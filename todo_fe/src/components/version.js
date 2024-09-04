import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';

export default async function Version() {
    const baseUrl = process.env.NEXT_PUBLIC_API_BASE_URL;
    const res = await fetch(`${baseUrl}/version`);
    const { version } = await res.json();
    
    return (
        <Container maxWidth="sm" style={{ marginTop: '2rem' }}>
            <Card variant="outlined">
                <CardContent>
                <Typography variant="h4" component="h1" gutterBottom>
                    Really Ugly Todo app
                </Typography>
                <Typography variant="body1" color="text.secondary">
                    Current Version: {version}
                </Typography>
                </CardContent>
            </Card>
        </Container>
    );
}