import React, { useState } from "react";
import { Input, Button, Container } from '@material-ui/core';

function Model() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    function validateForm() {
        return email.length > 0 && password.length > 0;
    }

    function handleSubmit(event) {
        event.preventDefault();
        console.log(event)
    }
    return (
    <Container maxWidth="xl">
        <form onSubmit={handleSubmit}>
            <Input type='email' placeholder="E-mail" inputProps={{ 'aria-label': 'description' }} onChange={(e) => setEmail(e.target.value)}/>
            <Input type='password' inputProps={{ 'aria-label': 'description' }} onChange={(e) => setPassword(e.target.value)}/>
            <Button type="submit" disabled={!validateForm()}>Login</Button>
        </form>
    </Container>
    );
}

export default Model;