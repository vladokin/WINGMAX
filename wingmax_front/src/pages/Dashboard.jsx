import { useNavigate } from 'react-router-dom'
import React from 'react'
import AdminDash from '../layouts/AdminDash'

function Dashboard() {
    const userInfo = JSON.parse(localStorage.getItem('userInfo'))
    const userRole = userInfo.role
    const navigate = useNavigate()
  return (
    userRole === 'Administrator' ? <AdminDash/> : userRole === 'Customer' ? <div>CustomerDash</div> : userRole === 'Airline' ? <div>AirlineDash</div> : navigate('/login')
  )
}

export default Dashboard