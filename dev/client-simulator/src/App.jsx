import {
    AppBar,
    Avatar,
    Box,
    Menu,
    MenuItem,
    Toolbar,
    Tooltip,
    Typography,
    IconButton,
    FormControl,
    Select,
    InputLabel,
    Container,
} from "@mui/material";
import { useState } from "react";
import IPComp from "./components/IPComp";
import URLComp from "./components/URLComp";

function App() {
    const [type, setType] = useState("");

    const handleChange = (event) => {
        setType(event.target.value);
    };
    return (
        <>
            <Box sx={{ flexGrow: 1 }}>
                <AppBar position="static">
                    <Toolbar>
                        <Typography
                            variant="h6"
                            component="div"
                            sx={{ flexGrow: 1 }}>
                            News
                        </Typography>
                        <Box
                            sx={{
                                flexGrow: 0,
                                width: "10rem",
                                color: "white",
                            }}>
                            <FormControl fullWidth>
                                <InputLabel
                                    id="demo-simple-select-label"
                                    sx={{ color: "inherit" }}>
                                    Type
                                </InputLabel>
                                <Select
                                    labelId="demo-simple-select-label"
                                    id="demo-simple-select"
                                    value={type}
                                    label="Type"
                                    sx={{
                                        backgroundColor: "inherit",
                                        color: "inherit",
                                    }}
                                    onChange={handleChange}>
                                    <MenuItem value={"url"}>URL</MenuItem>
                                    <MenuItem value={"ipAddress"}>
                                        IP Address
                                    </MenuItem>
                                </Select>
                            </FormControl>
                        </Box>
                    </Toolbar>
                </AppBar>
            </Box>
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
