import { useEffect,useState } from "react"
import { Navigate,useNavigate } from "react-router-dom"
import api from "../services/api"
import '../styles/dashboard.css'
export default function Dashboard(){
    const[urls,setUrls]=useState([])
    const[originalurl,setOriginalurl]=useState("")
    const[editingid,setEditingid]=useState(null)
    const navigate=useNavigate()
    useEffect(()=>{fetchurls()},[])
    const createurl=async(e)=>{
        e.preventDefault()
        try{
            if(editingid) await api.put(`shorten/${editingid}/`,{original_url:originalurl})
            else await api.post("shorten/",{original_url:originalurl})
            setOriginalurl("")
            setEditingid(null)
            fetchurls()
        }
        catch(error){console.log(error.response?.data)}
    }
    const fetchurls=async()=>{
        try{
            const response=await api.get("shorten/")
            setUrls(response.data)
        }
        catch(error){console.log(error)}
    }
    const handledelete=async(id)=>{
        try{
            await api.delete(`shorten/${id}/`)
            fetchurls()
        }
        catch(error){console.log(error.response?.data)}
    }
    const handleedit=(url)=>{
        setEditingid(url.id)
        setOriginalurl(url.original_url)
    }
    const handlelogout=()=>{
        localStorage.clear()
        navigate("/")
    }
    return(
        <div className="dashboard">
            <div className="dashboard-header">
                <h1>Dashboard</h1>
                <button onClick={handlelogout}  className="logout-btn">logout</button>
            </div>
            <form action="" onSubmit={createurl} className="url-form">
                <input type="url" placeholder="enter url" value={originalurl} onChange={(e)=>setOriginalurl(e.target.value)}/>
                <button type="submit">{editingid?"update":"shorten"}</button>
            </form>
            <div className="url-list">
                {urls.length===0?(
                    <p>No URLs created yet🙁</p>
                ):(
                    urls.map((url)=>(
                <div key={url.id} className="url-card">
                    <p><strong>original:</strong> {url.original_url}</p>
                    <p><strong>short:</strong> {url.short_url}</p>
                    <p><strong>clicks:</strong> {url.clicks}</p>
                    <div className="card-buttons">
                        <button onClick={()=>handleedit(url)} className="edit-btn">edit</button>
                        <button onClick={()=>handledelete(url.id)} className="delete-btn">delete</button>
                    </div>
                </div>
                )
            ))}
            </div>
        </div>
    )
}