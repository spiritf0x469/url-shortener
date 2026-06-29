import { Link } from "react-router-dom"
import '../styles/home.css'
export default function Home(){
    return(
        <div className="home">
            <div className="home-card">
                <h1 className="logo">🔗 URL Shortener</h1>
            <p className="subtitle">
                Shorten,long URLs into clean shareable links.
                Manage your links securely and track click analytics with ease.
            </p>
            <div className="buttons">
                <Link to="/login" className="btn">login</Link>
                <Link to="/register" className="btn">register</Link>
            </div>
            <div className="features">
                <div className="feature">🔒 JWT Authentication</div>
                <div className="feature">⚡ Fast Redirects</div>
                <div className="feature">📈 Click Tracking</div>
                <div className="feature">🌐 URL Management</div>
            </div>
            </div>
        </div>
    )
}