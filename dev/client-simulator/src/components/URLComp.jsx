import { Box, Button, FormControl, FormGroup, TextField } from "@mui/material";
import React, { useState } from "react";
import axios from "axios";

const URLComp = () => {
    const [url, setUrl] = useState("");
    const [result, setResult] = useState("Predict First");
    const handleSubmit = async () => {
        try {
            const response = await axios.post("http://127.0.0.1:3500/predict/url", {
                urls: [url],
            });
            setResult(response.data.prediction[0][url]);
        } catch (e) {
            console.log(e);
        }
    };
    return (
        <>
            <h1>URL Simulator</h1>
            <Box maxWidth={"100%"}>
                <FormControl sx ={{width: "100%"}}>
                    <FormGroup>
                        <label
                            htmlFor="urlInput"
                            style={{ fontSize: "1.2rem" }}>
                            URL:{" "}
                        </label>
                        <TextField
                            id="urlInput"
                            label="Url"
                            fullWidth
                            onChange={(e) => setUrl(e.target.value)}
                        />
                    </FormGroup>
                </FormControl>
            </Box>
            <Box mt="2rem">
                <Button variant="contained" onClick={handleSubmit}>
                    Send
                </Button>
            </Box>
            <Box>
                <p style={{ fontSize: "1.2rem" }}>
                    <b>Url Status: </b> {result}
                </p>
            </Box>
        </>
    );
};

export default URLComp;
