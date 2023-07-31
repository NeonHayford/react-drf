// import './App.css';
import React from 'react';
import { useState } from 'react';
import './input.css';
import axios from 'axios';

axios.default.xsrfCookieName = 'csrftoken';
axios.default.xsrfHeaderName = 'X-CSRFToken';
axios.default.withCredentials = true;


const client = axios.create({
  baseURL: 'http://127.0.0.1:8000'
});


// function handleClick(){
//   if (validateForm()) {
//     try {
//       const data = { name: username, email, password }
//     setLoading(!loading)
//       const response = client.post('registerUser', data)
//       if(response.data.success === true){
//         Cookies.set('userId', response.data.user._id)
//         toast.success('account created successfully')
//       setTimeout(() => {
//         dispatch(increaseCount())
//       }, 4000);
//     }
//     setTimeout(() => {
//       setLoading(true)
//     }, 4000);
      
//     } catch (error) {
//       const err = error.response.data.message
//       toast.warn(err)
//       setTimeout(() => {
//         setLoading(true)
//       }, 5000);
//     }
    
//   }
// }


function Register() {
  const [currentUser, setCurrentUser] = useState();
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');


  function submitRegistration(e){
    e.preventDefault();
    client.post('/api/signup', {
        username: username,
        email: email,
        password: password
      }
    ).then(function(response){
      setCurrentUser(true); 
    });
  }
  
  


  return (
    <div  className="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
        <div className="sm:mx-auto sm:w-full sm:max-w-sm">
          <img
            className="mx-auto h-10 w-auto"
            width="96"
            height="96"
            src="https://img.icons8.com/windows/96/term.png"
            alt="term"
          />
          <h2 className="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">
            Sign up to your account
          </h2>
        </div>

        

        <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
          <form onSubmit={submitRegistration} className="space-y-6" action="#" method="POST">

          <div>
              <label htmlFor="username" className="block text-sm font-medium leading-6 text-gray-900">
                Username
              </label>
              <div className="mt-2">
                <input
                  id="username"
                  name="username"
                  type="text"
                  onChange={e=>setUsername(e.target.value)}
                  required
                  className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                />
              </div>
            </div>

            <div>
              <label htmlFor="email" className="block text-sm font-medium leading-6 text-gray-900">
                Email
              </label>
              <div className="mt-2">
                <input
                  id="email"
                  name="email"
                  type="email"
                  onChange={e=>setEmail(e.target.value)}
                  autoComplete="email"
                  required
                  className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                />
              </div>
            </div>

            <div>
              <div className="flex items-center justify-between">
                <label htmlFor="password" className="block text-sm font-medium leading-6 text-gray-900">
                  Password
                </label>
              </div>
              <div className="mt-2">
                <input
                  id="password"
                  name="password"
                  type="password"
                  onChange={e=>setPassword(e.target.value)}
                  autoComplete="current-password"
                  required
                  className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                />
              </div>
            </div>

            <div>
              <button
                type="submit"
                className="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
              >
                Sign up
              </button>
            </div>
          </form>

          <p className="mt-10 text-center text-sm text-gray-500">
            Do you already have an account? {'  '}
            <a href="./signin" className="font-semibold text-indigo-600 hover:text-indigo-500">
              Sign In
            </a>
          </p>
        </div>
      </div>
  );
}
 

export default Register;
