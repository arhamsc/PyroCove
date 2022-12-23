import { Box, Button, FormControl, FormGroup, TextField } from "@mui/material";
import React, { useState } from "react";
import axios from "axios";

const IPComp = () => {
    const [ip, setIp] = useState("");
    const [result, setResult] = useState("Predict First");
    const handleSubmit = async () => {
        try {
            const response = await axios.post("http://127.0.0.1:3500/predict/ip", {
                ips: [ip],
            });
            setResult(response.data.prediction[0][ip]);
            console.log(response.data.prediction[0]);
        } catch (e) {
            console.log(e);
        }
    };
    return (
        <>
            <h1>IP Simulator</h1>
            <Box maxWidth={"100%"}>
                <FormControl sx={{ width: "100%" }}>
                    <FormGroup>
                        <label htmlFor="ipInput" style={{ fontSize: "1.2rem" }}>
                            IP:
                        </label>
                        <TextField
                            id="ipInput"
                            label="IP"
                            fullWidth
                            onChange={(e) => setIp(e.target.value)}
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
                    <b>IP Status: </b> {result}
                </p>
            </Box>
        </>
    );
};

export default IPComp;
