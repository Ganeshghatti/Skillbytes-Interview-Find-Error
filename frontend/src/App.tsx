import UsersPage from "./pages/UsersPage";

function App() {
  return (
    <div className="app-shell">
      <header className="app-header">
        <span className="app-header__brand">SkillBytes Admin</span>
      </header>
      <main className="app-main">
        <UsersPage />
      </main>
    </div>
  );
}

export default App;
