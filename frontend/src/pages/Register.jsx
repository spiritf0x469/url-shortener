import { useState } from "react"
import api from "../services/api"
import '../styles/auth.css'
import { Link } from "react-router-dom"
export default function Register(){
    const [username,setUsername]=useState("")
    const [password,setPassword]=useState("")
    const handlesubmit=async(e)=>{
        e.preventDefault()
        try{
            await api.post("register/",{username,password})
            alert("Registration successful!")
        }
        catch(error){
            console.log(error.response?.data)
            alert("Registration failed")
        }
    }
    return(
        <div className="auth">
            <div className="auth-card">
                <h1>REGISTER</h1>
                <form action="" onSubmit={handlesubmit} className="auth-form">
            <input type="text" placeholder="username" value={username} onChange={(e)=>setUsername(e.target.value)} />
            <input type="text" placeholder="password" value={password} onChange={(e)=>setPassword(e.target.value)} />
            <button type="submit">register</button>
        </form>
        <p className="auth-footer">
            Already have an account? <Link to="/login">Login</Link>
        </p>
            </div>
        </div>
    )
}