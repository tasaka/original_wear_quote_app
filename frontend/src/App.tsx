import { useEffect, useState } from "react";
import "./App.css";

const App = () => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/", { method: "GET" })
      .then((res) => res.json())
      .then((data) => {
        setPosts(data);
        console.log(data);
      });
  }, []);

  return (
    <div className="App">
      <h1>オリジナルウェア見積フォーム</h1>
      <div>
        <span>{posts.username}</span>
      </div>
    </div>
  );
};

export default App;
