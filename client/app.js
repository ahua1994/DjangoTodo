const baseUrl = `http://127.0.0.1:8000/`;
async function getTodos() {
    const res = await axios.get(baseUrl + "list/");
    console.log(res.data);
}
async function addTodo() {
    await axios.post(baseUrl + "todos/create/", {
        task: "learn vue",
        desc: "many job postings require this skill",
        priority: "M",
        done: false,
    });
}

getTodos();

document.getElementById("add-todo").addEventListener("click", () => {
    addTodo();
});
