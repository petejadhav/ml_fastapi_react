import React, { useState } from "react";
import { TextField, Button, Grid } from '@material-ui/core';
import {useRecoilValue} from 'recoil';
import {userState} from './state'

function Model() {
    const [Age, setAge] = useState("");
    const user = useRecoilValue(userState);
    const [modelScore, setModelScore] = useState("");

    function validateForm() {
        return Age > 0 && Age < 125;
    }

    function sendRequest() {
        fetch('/api/model?item_id='+Age, {
            method: 'GET',
            headers: {
              'Authorization': 'Bearer ' + user['token']
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            setModelScore(data['item_id']); 
            console.log(modelScore)          
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }

    function handleSubmit(event) {
        event.preventDefault();
        sendRequest();
        console.log(Age)
    }
    return (
    <Grid container direction="row" justify="center" alignItems="center" >        
        <TextField type='number' placeholder="Age" inputProps={{ 'aria-label': 'description' }} onChange={(e) => setAge(e.target.value)}/>
        <Button disabled={!validateForm()} onClick={handleSubmit}>Get Scores</Button>        
    </Grid>
    );
}

export default Model;