import TodoTile from "@/components/todoTile";
import { Container, Grid2, Typography, Box } from "@mui/material";

export default async function TodosPage () {
    const baseUrl = process.env.NEXT_PUBLIC_API_BASE_URL;
    const res = await fetch(`${baseUrl}/todos`);
    const { todos } = await res.json();
    return (
        <Container maxWidth="md" style={{ marginTop: '2rem' }}>
          <Grid2 container spacing={3}>
            {todos.length > 0 ? (
              todos.map((todo) => (
                <Grid2 item xs={12} sm={6} md={4} key={todo.uuid}>
                  <TodoTile todo={todo} />
                </Grid2>
              ))
            ) : (
              <Typography variant="body1">No todos found.</Typography>
            )}
          </Grid2>
        </Container>
      );
  };