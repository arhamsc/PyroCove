import {
    AppBar,
    Avatar,
    Box,
    FormControl,
    InputLabel,
    MenuItem,
    Select,
    Toolbar,
    Typography,
} from "@mui/material";
import logo from "../assets/logo.png"
import logoText from "../assets/logo_png.png"

export const NavBar = ({handleChange, type}) => {
    return (
        <Box sx={{ flexGrow: 1, height: "5rem" }}>
            <AppBar position="static" sx={{ height: "100%" }}>
                <Toolbar sx={{ height: "100%" }}>
                    <Box flexGrow={1} display="flex" alignItems={"center"}>
                        <Avatar
                            src={logo}
                            sx={{ width: "3rem", height: "100%" }}
                        />
                        <img src={logoText} width="10%" height="20%" />
                    </Box>
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
    );
};
