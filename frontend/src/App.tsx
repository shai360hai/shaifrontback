import Login from './pages/login';
import Register from './pages/RegisterForm';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

export default function App() {
  return (
          <BrowserRouter>
              <Routes>
                  <Route path="/register" element={<Register />} />
                  <Route path="/login" element={<Login />} />
              </Routes>
          </BrowserRouter>
  )
}