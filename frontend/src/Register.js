import React, { useState } from "react";
import { TextField, Button, Grid, Paper } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import { useHistory } from "react-router-dom";
import {useRecoilState} from 'recoil';
import {userState} from './state'

const useStyles = makeStyles({
    root: {
      background: '#fff',
      width: '40%',
      'min-width': '320px',
      'max-width': '475px',
      padding: '8px',
      position: 'relative',
      display: 'flex',
       'align-items': 'center',
        'justify-content': 'center',
    },
    button: {
        background: 'linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%)',
        width:'50%',
        //position: 'absolute',
        //top: '70%',
    },
    input: {
        width: '100%',
        'padding-bottom': '8px'
    }
});

function Register() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const classes = useStyles();
    let history = useHistory();
    const [user, setUser] = useRecoilState(userState);

    function registerUser(){
        fetch('http://localhost:8000/register', {
            method: 'POST',
            mode: 'cors',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({'email':email, 'password':password}) // body data type must match "Content-Type" header
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            setUser({
                'authenticated':true,
                'user':email,
                'password': password,
                'token': data['access_token']
            });            
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }

    function validateForm() {
        return email.length > 0 && password.length > 0 && password === confirmPassword;
    }

    function handleSubmit(event) {
        event.preventDefault();
        registerUser();
        history.push("/model")
    }
    return (
    <Grid container direction="row" justify="center" alignItems="center" >
        <Paper className={classes.root}>
            <form onSubmit={handleSubmit}>
                <TextField className={classes.input} type='email' label="E-mail" variant="outlined" color="secondary" inputProps={{ 'aria-label': 'description' }} onChange={(e) => setEmail(e.target.value)}/>
                <TextField className={classes.input} type='password' label="Password" variant="outlined" color="secondary" inputProps={{ 'aria-label': 'description' }} onChange={(e) => setPassword(e.target.value)}/>
                <TextField className={classes.input} type='password' label="Confirm Password" variant="outlined" color="secondary" inputProps={{ 'aria-label': 'description' }} onChange={(e) => setConfirmPassword(e.target.value)}/>
                <Button className={classes.button} type="submit" disabled={!validateForm()}>Register</Button>
            </form>
        </Paper>
    </Grid>    
    
    );
}

export default Register;