import { useEffect } from "react"

export default function Home() {
    useEffect(() => {
        checkAuth()
    }, [])

    return (
        <div id="status">Home</div>
    )
}

async function checkAuth() {
    const response = await fetch("http://localhost:8000/users/me", {
        credentials: "include"
    })

    if (!response.ok) {
        window.location.href = "/login"
        return
    }

    const user = await response.json()
    console.log(user)
}
