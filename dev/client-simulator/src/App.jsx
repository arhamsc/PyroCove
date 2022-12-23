import {
    AppBar,
    Box,
    MenuItem,
    Toolbar,
    Typography,
    FormControl,
    Select,
    InputLabel,
    Container,
} from "@mui/material";
import { useState } from "react";
import IPComp from "./components/IPComp";
import { NavBar } from "./components/NavBar";
import URLComp from "./components/URLComp";

function App() {
    const [type, setType] = useState("");

    const handleChange = (event) => {
        setType(event.target.value);
    };
    return (
        <>
            <NavBar handleChange={handleChange} type={type} />
            <Container>
                {type == "url" ? (
                    <URLComp />
                ) : type == "ipAddress" ? (
                    <IPComp />
                ) : (
                    <h1>Select a choice</h1>
                )}
            </Container>
        </>
    );
}

export default App;
