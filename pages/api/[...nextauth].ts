import { NextApiRequest, NextApiResponse } from "next";
import NextAuth from "next-auth";
import { NextAuthOptions } from "next-auth";
import GoogleProvider from "next-auth/providers/google";
import axios from "axios";
import { JwtUtils, UrlUtils } from "../../constants/Utils";

const settings: NextAuthOptions = {

    secret: process.env.SESSION_SECRET,
    session: {
      jwt: true,
      maxAge: 24 * 60 * 60, // 24 hours
    },
    jwt: {
      secret: process.env.JWT_SECRET,
    },
    debug: process.env.NODE_ENV === "development",
    providers: [
        GoogleProvider({
          clientId: process.env.GOOGLE_CLIENT_ID,
          clientSecret: process.env.GOOGLE_CLIENT_SECRET,
        }),
      ],
      callbacks: {
        async signIn(user,account,profile) {
            return true;
        },
        async jwt(token, user, account, profile, isNewUser) {
            if (user) {
                if (account.provider === "google") {
                    const { accessToken, idToken } = account;

                    try {
                        const response = await axios.post(
                            UrlUtils.makeUrl(
                                process.env.BACKEND_API_BASE,
                                "social",
                                "login",
                                account.provider,
                              ),
                              {
                                access_token: accessToken, // note the differences in key and value variable names
                                id_token: idToken,
                              },
                            ); 

                            const { access_token, refresh_token } = response.data;
                            token = {
                                ...token,
                                accessToken: access_token,
                                refreshToken: refresh_token,
                              };
                            
                              return token;
                            } catch (error) {
                               return null;
                            }
                        }
                    }

      if (JwtUtils.isJwtExpired(token.accessToken as string)) {
        const [
          newAccessToken,
          newRefreshToken,
        ] = await NextAuthUtils.refreshToken(token.refreshToken);

        if (newAccessToken && newRefreshToken) {
          token = {
            ...token,
            accessToken: newAccessToken,
            refreshToken: newRefreshToken,
            iat: Math.floor(Date.now() / 1000),
            exp: Math.floor(Date.now() / 1000 + 2 * 60 * 60),
          };

          return token;
        }
        
        return {
            ...token,
            exp: 0,
          };
        }
  
        // token valid
        return token;
      },
  
        
        async session  (session,user) {
            session.accessToken = user.accessToken;
            return session;
        }
    }
}

export default (req: NextApiRequest, res: NextApiResponse)=> NextAuth(req,res,settings);