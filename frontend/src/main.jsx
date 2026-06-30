import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './styles/global.css'
import App from './App.jsx'
import 'react-toastify/dist/ReactToastify.css'
import {ToastContainer} from "react-toastify"

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
    <ToastContainer
      position='top-right'
      autoClose={2500}
      theme='dark'
    />
  </StrictMode>,
)
