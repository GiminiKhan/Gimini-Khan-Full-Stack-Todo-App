"use client";
import { useState } from "react";
export default function LoginPage() {
  const [form, setForm] = useState({ email: "", password: "" });
  const handleLogin = async (e) => {
    e.preventDefault();
    const res = await fetch("http://127.0.0.1:8000/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form)
    });
    if (res.ok) {
      const data = await res.json();
      localStorage.setItem("access_token", data.access_token || data.token);
      window.location.href = "/dashboard";
    } else {
      const err = await res.json();
      alert("Login Failed: " + (err.detail || "Check email/password"));
    }
  };
  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-100">
      <form onSubmit={handleLogin} className="bg-white p-10 rounded-3xl shadow-xl w-96">
        <h2 className="text-3xl font-bold mb-8 text-center text-indigo-600">Login</h2>
        <input className="w-full p-4 mb-4 border rounded-xl text-black" type="email" placeholder="Email (test@example.com)" onChange={e => setForm({...form, email: e.target.value})} required />
        <input className="w-full p-4 mb-8 border rounded-xl text-black" type="password" placeholder="Password" onChange={e => setForm({...form, password: e.target.value})} required />
        <button type="submit" className="w-full bg-indigo-600 text-white p-4 rounded-xl font-bold">SIGN IN</button>
      </form>
    </div>
  );
}