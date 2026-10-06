import { Mail, KeyRound, ArrowRight, UserPlus } from "lucide-react"

function Login() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-(--secondary)">
      <div className="p-8 rounded-lg flex flex-col items-center justify-center bg-(--background)">
        <h1 className="text-3xl text-(--text-primary) font-bold">Bem-vindo de volta!</h1>
        <p className="mt-2 text-(--text-secondary)">Faça login para acessar sua conta no SamBank.</p>

        <form className="flex w-full flex-col">

          {/*Input de email*/}
          <div className="mt-3">
            <label className="text-(--text-primary)">E-mail</label>
            <div className="flex flex-row border text-(--border) rounded-lg p-3">
              <Mail className="text-(--text-secondary) me-3 p-0.5"></Mail>
              <input className="text-(--text-secondary) outline-none" type="email" placeholder="Digite seu E-mail"></input>
            </div>
          </div>

          {/*Input de senha*/}
          <div className="mt-3">
            <label className="text-(--text-primary)">Senha</label>
            <div className="flex flex-row border text-(--border) rounded-lg p-3">
              <KeyRound className="text-(--text-secondary) me-3 p-0.5"></KeyRound>
              <input className="text-(--text-secondary) outline-none" type="password" placeholder="••••••••••••••"></input>
            </div>
          </div>

          {/*Checkbox lembrar de mim*/}
          <div className="flex mt-4 text-start gap-2 items-center">
            <input type="checkbox" className="size-4 accent-(--success)"></input>
            <label className="text-sm">Lembrar de mim</label>
          </div>

          {/*Botão de entrar*/}
          <div className="flex w-full mt-4 gap-2 bg-(--primary) justify-center p-3 rounded-lg">
            <button type="submit" className="text-(--text-inverse)">Entrar</button>
            <ArrowRight className="text-(--text-inverse)"></ArrowRight>
          </div>

          {/*Separator*/}
          <div className="flex items-center my-3 gap-4">
            <div className="h-px w-full bg-(--border)" />
            <span className="text-(--text-secondary)">ou</span>
            <div className="h-px w-full bg-(--border)" />
          </div>

          {/*Botão de Criar conta*/}
          <div className="flex w-full gap-2 border-2 border-(--border) justify-center p-3 rounded-lg">
            <UserPlus className="text-(--text-secondary)"></UserPlus>
            <button type="submit" className="text-(--text-prmiary)">Criar conta</button>
          </div>


        </form>
      </div>
    </div>
  )
}

export default Login
