****<h1 align="center" style="font-weight: bold;">Python Back-end 💻</h1>

<p align="center">
 <a href="#tech">Technologies</a> • 
 <a href="#started">Getting Started</a> • 
  <a href="#routes">API Endpoints</a> 
  <a href="#swagger">Swagger</a> •
 <a href="#colab">Collaborators</a> •
 <!-- <a href="#contribute">Contribute</a> -->
</p>

<p align="center">
    <b>Simple description of what your project do or how to use it.</b>
</p>
<h2 id="tech">💻 Technologies</h2>

- list of all technologies you used
- Python
- Flask
- Sql

<h2 id="started">🚀 Getting started</h2>

Here you describe how to run your project locally

<h3>Prerequisites</h3>

Here you list all prerequisites necessary for running your project:

- [Python](https://www.python.org)
- [Flask](https://github.com)
- [MySql](https://www.mysql.com)

<h3>Cloning</h3>

How to clone your project


```bash
git clone git@github.com:rcrossa/pythonbackend.git
```

<h3>Starting</h3>

How to start your project

```bash
- cd project-name
- python3 -m venv venv
- source venv/bin/activate 
- pip install -r requirement.txt
```
<b>Observation: if you have any error related python dependency please intall manually.</b>

<h3>Dotenv</h3>
<b>Create an .env file in root directory and you need to complete the following information related to the database:</b> 

```bash
- DB_USERNAME=the username 
- DB_PASSWORD=the password 
- DB_HOST= the hostname 
- DB_PORT=the port 
- DB_NAME= the name 
```


 <h2 id="routes">📍 API Endpoints</h2>

The following endpoints are available:
​
| route               | description                                          
|----------------------|-----------------------------------------------------
| <kbd>GET /</kbd>     | retrieve a text example [response details](#get-text)
| <kbd>GET /api/movies</kbd>     | retrieve an object [response details](#get-object)
| <kbd>GET /api/movies/{id}</kbd>     | retrieve an object [response details](#get-movieby-id)
| <kbd>POST /api/movies/</kbd>     | retrieve a response [response details](#create-movie)
| <kbd>PUT /api/movies/{id}</kbd>     | retrieve a response [response details](#get-movie)
| <kbd>DELETE /api/movies/{id}</kbd>     | retrieve a response [response details](#delete-movie)


<h3 id="get-text">GET /</h3>

**RESPONSE**
```html
<h1>Hola mundo con flask 🐍</h1>
```
<h3 id="get-object">GET /api/movies</h3>

**RESPONSE**
```json
[
    {
        "banner": "1",
        "director": "teste",
        "id_movie": 1,
        "rating": "3",
        "release_date": "Fri, 22 Mar 2222 00:00:00 GMT",
        "title": "teste"
    }
]
```
<h3 id="get-movieby-id">GET /api/movies/{id}</h3>

**RESPONSE**
```json
{
    "banner": "1",
    "director": "teste",
    "id_movie": 1,
    "rating": [
        3
    ],
    "release_date": "Fri, 22 Mar 2222 00:00:00 GMT",
    "title": "teste"
}
```
<h3 id="create-movie">POST /api/movies/</h3>

**RESPONSE**
```json
{
    "response": "Movie created successfully"
}
```
<h3 id="update-movie">PUT /api/movies/{id}</h3>

**RESPONSE**
```json
{
    "banner": "1",
    "director": "teste",
    "id_movie": 1,
    "rating": [
        3
    ],
    "release_date": "Fri, 22 Mar 2222 00:00:00 GMT",
    "title": "teste"
}
```
<h3 id="delete-movie">DELETE /api/movies/{id}</h3>

**RESPONSE**
```json
{
  "response": "Movie deleted successfully"
}
```

<h3 id="swagger">Swagger</h3>
<h4>You can see information related to swagger in the path: /swagger</h4>


<h2 id="colab">🤝 Collaborators</h2>

Special thank you for all people that contributed for this project.

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/28865492?v=4" width="100px;" alt="Roberto Rossa Profile Picture"/><br>
        <sub>
          <b>Roberto Rossa</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/49814034?v=4" width="100px;" alt="Jose Arrese Profile Picture"/><br>
        <sub>
          <b>Jose Arrese</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/20940000?v=4" width="100px;" 
        alt="Lucas Giurastante Profile Picture"/><br>
        <sub>
          <b>Lucas Giurastante</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

<!-- <h2 id="contribute">📫 Contribute</h2>

Here you will explain how other developers can contribute to your project. For example, explaining how can create their branches, which patterns to follow and how to open an pull request

1. `git clone https://github.com/Fernanda-Kipper/text-editor.git`
2. `git checkout -b feature/NAME`
3. Follow commit patterns
4. Open a Pull Request explaining the problem solved or feature made, if exists, append screenshot of visual modifications and wait for the review!

<h3>Documentations that might help</h3>

[📝 How to create a Pull Request](https://www.atlassian.com/br/git/tutorials/making-a-pull-request)

[💾 Commit pattern](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716) -->