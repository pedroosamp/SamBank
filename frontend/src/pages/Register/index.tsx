import { Mail, Lock, ArrowRight, UserPlus } from "lucide-react"

export default function Register() {
    return (
    <div className="min-h-screen flex flex-col shadow-xl items-center justify-center bg-(--border)">
        <div className="w-120 p-8 rounded-lg flex flex-col items-center justify-center bg-(--background)">
            <div className="flex flex-col items-center text-center-72">
                <h1 className="text-3xl text-(--text-primary) font-bold">Welcome!</h1>
                <p className="mt-2 text-(--text-secondary) max-w-64 text-center">Create a SamBank account.</p>
            </div>

            <form id="registerForm" className="grid grid-cols-12 w-full mt-3 gap-3" onSubmit={handleRegister}>
                <div className="col-span-6">
                    <label className="text-(--text-primary)">First name</label>
                    <div className="flex flex-row border text-(--border) rounded-lg p-3">
                        <input className="text-(--text-secondary) outline-none w-full" name="first_name" type="text" placeholder="John"></input>
                    </div>
                </div>

                <div className="col-span-6">
                    <label className="text-(--text-primary)">Last name</label>
                    <div className="flex flex-row border text-(--border) rounded-lg p-3">
                        <input className="text-(--text-secondary) outline-none w-full" name="last_name" type="text" placeholder="Doe"></input>
                    </div>
                </div>

                <div className="col-span-6">
                    <label className="text-(--text-primary)">Birthday</label>
                    <div className="flex flex-row border text-(--border) rounded-lg p-3">
                        <input className="text-(--text-secondary) outline-none w-full" name="birthday" type="date"></input>
                    </div>
                </div>

                <div className="col-span-6">
                    <label className="text-(--text-primary)">Phone number</label>
                    <div className="flex flex-row border text-(--border) rounded-lg p-3">
                        <input className="text-(--text-secondary) outline-none w-full" name="phone_number" type="text" placeholder="+1 (123) 456 7890"></input>
                    </div>
                </div>

                <div className="col-span-6">
                    <label className="text-(--text-primary)">E-mail</label>
                    <div className="flex flex-row border text-(--border) rounded-lg p-3">
                        <Mail className="text-(--text-secondary) me-3 p-0.5"></Mail>
                        <input className="text-(--text-secondary) outline-none w-full" name="email" type="email" placeholder="Digite seu e-mail"></input>
                    </div>
                </div>

                <div className="col-span-6">
                    <label className="text-(--text-primary)">National ID number</label>
                    <div className="flex flex-row border text-(--border) rounded-lg p-3">
                        <input className="text-(--text-secondary) outline-none w-full" name="national_id" type="text" placeholder="12.345.678-9"></input>
                    </div>
                </div>

                <div className="col-span-12">
                    <label className="text-(--text-primary)">Password</label>
                    <div className="flex flex-row border text-(--border) rounded-lg p-3">
                        <Lock className="text-(--text-secondary) me-3 p-0.5"></Lock>
                        <input className="text-(--text-secondary) outline-none w-full" name="password" type="password" placeholder="••••••••••••"></input>
                    </div>
                </div>

                {/*<div className="col-span-6">
                    <label className="text-(--text-primary)">Confirm password</label>
                    <div className="flex flex-row border text-(--border) rounded-lg p-3">
                        <Lock className="text-(--text-secondary) me-3 p-0.5"></Lock>
                        <input className="text-(--text-secondary) outline-none w-full" type="password" placeholder="••••••••••••"></input>
                    </div>
                </div>*/}

                <div className="col-span-12">
                    <div className="flex mt-1 text-start gap-2 items-center">
                        <input type="checkbox" className="size-4 accent-(--success) hover:cursor-pointer"></input>
                        <label className="text-sm hover:cursor-pointer">Remember me</label>
                    </div>
                </div>

                <div className="col-span-12">
                    <button type="submit" className="flex w-full gap-2 bg-(--primary) justify-center p-3 rounded-lg text-(--text-inverse) hover:cursor-pointer">
                        <UserPlus className="text-(--text-inverse) hover:cursor-pointer"></UserPlus>
                        Create an account
                    </button>
                </div>
            </form>

            <div className="flex w-full">
                <div className="flex w-full items-center my-4 gap-4">
                <div className="h-px w-full bg-(--border)" />
                <span className="text-(--text-secondary)">or</span>
                <div className="h-px w-full bg-(--border)" />
                </div>
            </div>

            <a href="/login" className="text-(--text-primary) hover:cursor-pointer flex w-full gap-2 border-2 border-(--border) justify-center p-3 rounded-lg">
                I have an account
                <ArrowRight className="text-(--text-secondary) hover:cursor-pointer"></ArrowRight>
            </a>
        </div>
    </div>
  )
}

async function handleRegister(event: React.SubmitEvent<HTMLFormElement>) {
    event.preventDefault()

    const form = new FormData(event.currentTarget)

    const first_name = form.get("first_name")
    const last_name = form.get("last_name")
    const birthday = form.get("birthday")
    const phone_number = form.get("phone_number")
    const national_id = form.get("national_id")
    const email = form.get("email")
    const password = form.get("password")

    const response = await fetch("http://127.0.0.1:8000/users/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            first_name, last_name, birthday, phone_number, national_id, email, password
        })
    })

    const data = await response.json();
}
