import Version from "@/components/version";
import TodosPage from "@/components/todolist";
import { Container } from "@mui/material";

export default function Home() {
  return (
    <main>
      <Container maxWidth="sm" style={{ marginTop: "2rem" }}>
        <Version />
        <TodosPage />
      </Container>
    </main>
  );
}
