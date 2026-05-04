import { useEffect, useState } from "react";

function Todos() {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [input, setInput] = useState("");

  type Todo = {
    text: string;
  };

  // Fetch todos
  const fetchTodos = async () => {
    const response = await fetch("http://127.0.0.1:8000/todos");

    const data = await response.json();

    setTodos(data);
  };

  useEffect(() => {
    fetchTodos();
  }, []);

  // Add todo
  const addTodo = async () => {
    if (!input) return;

    await fetch("http://127.0.0.1:8000/todos", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        text: input,
      }),
    });

    setInput("");

    fetchTodos();
  };

  // Delete todo
  const deleteTodo = async (index: number) => {
    await fetch(`http://127.0.0.1:8000/todos/${index}`, {
      method: "DELETE",
    });

    fetchTodos();
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Todo Todos</h1>

      <input
        type="text"
        placeholder="Enter todo"
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />

      <button onClick={addTodo}>Add</button>

      <ul>
        {todos.map((todo, index) => (
          <li key={index}>
            {todo.text}

            <button onClick={() => deleteTodo(index)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Todos;
