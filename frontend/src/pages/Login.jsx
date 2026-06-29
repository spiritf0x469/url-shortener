import { useState } from "react"
import { useNavigate } from "react-router-dom"
import api from "../services/api"
import '../styles/auth.css'
import { Link } from "react-router-dom"
export default function Login(){
    const[username,setUsername]=useState("")
    const[password,setPassword]=useState("")
    const navigate=useNavigate()
    const handlesubmit=async(e)=>{
        e.preventDefault()
        try{
            const response=await api.post("token/",{
                username,password,
            })
            localStorage.setItem("access",response.data.access)
            localStorage.setItem("refresh",response.data.refresh)
            navigate("/dashboard")
        }
        catch(error){
            console.log(error.response?.data)
            alert("Invalid credentials")
        }
    }
    return(
        <div className="auth">
            <div className="auth-card">
                <h1>LOGIN</h1>
                <form action="" onSubmit={handlesubmit} className="auth-form">
            <input type="text" placeholder="username" value={username} onChange={(e)=>setUsername(e.target.value)} />
            <input type="password" placeholder="password" value={password} onChange={(e)=>setPassword(e.target.value)} />
            <button type="submit">login</button>
        </form>
        <p className="auth-footer">
            Don't have an account? <Link to="/register">Register</Link>
        </p>
            </div>
        </div>
    )
}