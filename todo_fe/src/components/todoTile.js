import { Box, Card, CardContent, Typography } from '@mui/material';
const TodoTile = ({ todo }) => {
    const { title, description, completed, createdAt, updatedAt } = todo;
  
    // Format the dates for display
    const formatDate = (dateString) => {
      return new Date(dateString).toLocaleString();
    };
  
    return (
        <Card
          variant="outlined"
          sx={{
            backgroundColor: completed ? '#e0ffe0' : '#f9f9f9',
            borderColor: completed ? '#00cc00' : '#ccc',
            marginBottom: '1rem',
            minWidth: 250,
          }}
        >
          <CardContent>
            <Typography variant="h5" component="h2" gutterBottom>
              {title}
            </Typography>
            <Typography variant="body2" color="text.secondary" gutterBottom>
              {description}
            </Typography>
            <Box mt={2}>
              <Typography variant="body1" fontWeight="bold">
                Status: {completed ? 'Completed' : 'Pending'}
              </Typography>
              <Typography variant="caption" display="block" color="text.secondary">
                Created At: {formatDate(createdAt)}
              </Typography>
              <Typography variant="caption" display="block" color="text.secondary">
                Last Updated: {formatDate(updatedAt)}
              </Typography>
            </Box>
          </CardContent>
        </Card>
      );
  };
  
  export default TodoTile;