
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
		  });
		fetchRes.then(res =>
			res.json()).then(d => {
				console.log(d)
			})			
}


async function login() {
	document.getElementById("status").innerText  = "loading"
    const csrfRes = await fetch("http://127.0.0.1:8000/getcsrf");
    const csrfData = await csrfRes.json();
    const csrfToken = csrfData.csrf_token;
    const headers = {
        "Content-Type": "application/json",
        "X-csrftoken": csrfToken
    };

    const fetchRes = await fetch("http://127.0.0.1:8000/login_user", {
        method: "POST",
        headers: headers,
        body: JSON.stringify({
            "password": document.getElementById("password").value,
            "email": document.getElementById("email").value,
            "name": "",
            "fromchrome": 0
        })
    });
    const responseData = await fetchRes.json();
	document.getElementById("status").innerText  = responseData.msg
}


function getUser(){
	let fetchRes = fetch(
		"http://127.0.0.1:8000/getuser",{
			method: "GET",	
			headers: {
			  "Content-Type": "application/json",
			},
		  });
		fetchRes.then(res =>
			res.json()).then(d => {
				console.log(d)
			})
}



function getting_started(){
	login()
	
}

getting_started()