import { signIn,signOut,useSession } from "next-auth/react";


export default function Home (){
    const {data: session, status="loading", update} = useSession();

    return (
        <>
        {
        status === "loading" && <h2>Loading...</h2>
}

{!(status === "loading") && !session && (
    <>
    Not Signed in <br />
    <button onClick={() => signIn()}>Sign In</button>
    <pre>{!session && "User is not logged in"}</pre>
    </>
)}

{!(status === "loading") && session && (
    <>
    Signed in as {session.user.email}<br />
    <button onClick = {() => signOut()}>SignOut</button>
    {
        session.accessToken && (
            <pre>User has access token</pre>
        )
    }
    </>
    )}
</>
    );
}
