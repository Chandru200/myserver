
async function postData(url = "", data = {}) {
	const response = await fetch(url, {
	  method: "POST",	
	  headers: {
		"Content-Type": "application/json",
	  },
	  body: JSON.stringify(data),
	});
	return response.json();
  }

async function getData(url = "", data = {}) {
const response = await fetch(url, {
	method: "GET",	
	headers: {
	"Content-Type": "application/json",
	},
});
return response.json();
}

document.getElementById("login").addEventListener("click", (e)=>{
	login()
});
document.getElementById("logout").addEventListener("click", (e)=>{
	logout()
});
document.getElementById("getuser").addEventListener("click", (e)=>{
	getUser()
});



function logout(){
	let fetchRes = fetch(
		"http://127.0.0.1:8000/logout",{
			method: "GET",	
			headers: {
			  "Content-Type": "application/json"
			},
			// body: JSON.stringify({
			// 	"password":"test1",
			// 	"email":"test1@gmail.com",
			// 	"name":"test1"
			// }),
		  });
		fetchRes.then(res =>
			res.json()).then(d => {
				console.log(d)
			})			
}

function login(){
	let fetchRes = fetch(
		"http://127.0.0.1:8000/login_user",{
			method: "POST",	
			headers: {
			  "Content-Type": "application/json",
			},
			body: JSON.stringify({
				"password":"new",
				"email":"new@gmail.com",
				"name":"new",
				"fromchrome":0
			}),
		  });
		fetchRes.then(res =>
			res.json()).then(d => {
				console.log(d)
			})
}

function getUser(){
	let fetchRes = fetch(
		"http://127.0.0.1:8000/getuser",{
			method: "GET",	
			headers: {
			  "Content-Type": "application/json",
			},
			// body: JSON.stringify({
			// 	"password":"test1",
			// 	"email":"test1@gmail.com",
			// 	"name":"test1"
			// }),
		  });
		fetchRes.then(res =>
			res.json()).then(d => {
				console.log(d)
			})
}