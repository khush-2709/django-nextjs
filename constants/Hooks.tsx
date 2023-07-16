// ### Failed approach using useState() ###
// export function useAuth(refreshInterval?: number): [Session, boolean] {
//   /*
//     custom hook that keeps the session up-to-date by refreshing it

//     @param {number} refreshInterval: The refresh/polling interval in seconds. default is 20.
//     @return {tuple} A tuple of the Session and boolean
//   */
//   const [session, setSession] = useState<Session>(null);
//   const [loading, setLoading] = useState<boolean>(false);

//   useEffect(() => {
//     async function fetchSession() {
//       let sessionData: Session = null;
//       setLoading(true);

//       const session = await getSession({});

//       if (session && Object.keys(session).length > 0) {
//         sessionData = session;
//       }

//       setSession((_) => sessionData);
//       setLoading(false);
//     }

//     refreshInterval = refreshInterval || 20;

//     fetchSession();
//     const interval = setInterval(() => fetchSession(), refreshInterval * 1000);

//     return () => clearInterval(interval);
//   }, []);

//   return [session, loading];
// }