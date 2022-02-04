<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <style>
        body {
            background-color: black;
        }
        input, button {
            margin: 5px;
            padding: 5px;
            font-family: monospace, monospace;
        }
        #container {
            display: flex;
            align-items: center;
            align-content: center;
            justify-content: center;
            text-align: center;
            margin-top: 10vh;
        }
        h1 {
            color: #FFE81F;
            font-family: monospace, monospace;
        }
    </style>
</head>
<body>
<div>
    <div id="container">
        <form action="/login" method="POST">
            <h1>May the force be with you</h1>
            <div>
                <input type="text" name="uname" placeholder="Username" />
            </div>
            <div>
                <input type="text" name="password" placeholder="Password" />
            </div>
            <button type="submit">Login</button>
        </form>
    </div>
</div>
</body>
</html>
