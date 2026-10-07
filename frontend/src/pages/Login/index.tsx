import { Mail, KeyRound, ArrowRight, UserPlus } from "lucide-react"

export default function Login() {
    return (
    <div className="min-h-screen flex flex-col shadow-xl items-center justify-center bg-(--border)">
        <div className="w-120 p-8 rounded-lg flex flex-col items-center justify-center bg-(--background)">
            <div className="flex flex-col items-center text-center-72">
                <h1 className="text-3xl text-(--text-primary) font-bold">Welcome back!</h1>
                <p className="mt-2 text-(--text-secondary) max-w-64 text-center">Login to your SamBank account.</p>
            </div>

            <form id="loginForm" className="flex w-full flex-col mt-3 gap-3" onSubmit={handleLogin}>
                <div>
                    <label className="text-(--text-primary)">E-mail</label>
                    <div className="flex flex-row border text-(--border) rounded-lg p-3">
                        <Mail className="text-(--text-secondary) me-3 p-0.5"></Mail>
                        <input className="text-(--text-secondary) outline-none w-full" name="email" type="email" placeholder="Digite seu e-mail"></input>
                    </div>
                </div>
                <div>
                    <label className="text-(--text-primary)">Password</label>
                    <div className="flex flex-row border text-(--border) rounded-lg p-3">
                        <KeyRound className="text-(--text-secondary) me-3 p-0.5"></KeyRound>
                        <input className="text-(--text-secondary) outline-none w-full" name="password" type="password" placeholder="••••••••••••"></input>
                    </div>
                </div>

                <div className="flex mt-1 text-start gap-2 items-center">
                    <input type="checkbox" className="size-4 accent-(--success)"></input>
                    <label className="text-sm">Remember me</label>
                </div>

                <button type="submit" className="flex w-full gap-2 bg-(--primary) justify-center p-3 rounded-lg text-(--text-inverse) hover:cursor-pointer">
                    Login
                    <ArrowRight className="text-(--text-inverse) hover:cursor-pointer"></ArrowRight>
                </button>
            </form>

            <div className="flex w-full">
                <div className="flex w-full items-center my-4 gap-4">
                <div className="h-px w-full bg-(--border)" />
                <span className="text-(--text-secondary)">or</span>
                <div className="h-px w-full bg-(--border)" />
                </div>
            </div>

            <a href="/register" className="text-(--text-primary) hover:cursor-pointer flex w-full gap-2 border-2 border-(--border) justify-center p-3 rounded-lg">
                <UserPlus className="text-(--text-secondary) hover:cursor-pointer"></UserPlus>
                I don't have an account
            </a>
        </div>
    </div>
  )
}

async function handleLogin(event: React.SubmitEvent<HTMLFormElement>) {
    event.preventDefault()

    const form = new FormData(event.currentTarget)
    const email = form.get("email")
    const password = form.get("password")

    const formData = new URLSearchParams()
    formData.append("username", email)
    formData.append("password", password)

    const response = await fetch("http://127.0.0.1:8000/auth/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: formData
    })

    const data = await response.json();
}
