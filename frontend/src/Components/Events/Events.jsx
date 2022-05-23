import React from "react";
import "./index.css";
import Element from "./Element";
import dbOptions from "../../dummydb/dbOptions.jsx"
import { Button, MenuItem, TextField } from "@material-ui/core";
import api from "../../Base/fetchData"

export default class Events extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            results: {"toanmath":"0"},
            type: "",
            subject: "",
            grade: "",
            level: "",
            text: "",
        }
        
    };
    
    componentDidMount = () => {
            this.doSearch();
        }
    

    handleChangeType(option){
        this.setState({type:option.target.value});
    };
    handleChangeSubjet(option){
        this.setState({subject:option.target.value});
    };
    handleChangeGrade(option){
        this.setState({grade:option.target.value});
    };
    handleChangeLevel(option){
        this.setState({level:option.target.value});
    };
    async doSearch(){
        var body = {
            "type": this.state.type,
            "subject": this.state.subject,
            "grade": this.state.grade,
            "level": this.state.level,
            "text": this.state.text,
            "page": this.state.page
        }
        try{
            var res = await api.searchall(body);
        }
        catch{
            var res = {"result": {"toanmath":"0"}}
        }
        this.setState({results:res.result})
    };
    render() {
        return (
            <div className="eventsChild">
                <div className="search-bar">
                    <h2>Tìm kiếm</h2>
                    <div>
                        <div className="filter-wrapper">
                            <div className="filter-type">
                                <TextField
                                    name="type"
                                    className="outlined-basic"
                                    variant="outlined"
                                    margin="dense"
                                    fullWidth
                                    label="Loại đề thi"
                                    select
                                    value={this.state.type}
                                    onChange={this.handleChangeType.bind(this)}
                                >
                                    {dbOptions.types.map((option) => (
                                    <MenuItem key={option.value} value={option.value}>
                                        {option.label}
                                    </MenuItem>
                                    ))}
                                </TextField>
                            </div>

                            <div className="filter-subject">
                                <TextField
                                    name="subject"
                                    className="outlined-basic"
                                    variant="outlined"
                                    margin="dense"
                                    fullWidth
                                    label="Môn học"
                                    select
                                    value={this.state.subject}
                                    onChange={this.handleChangeSubjet.bind(this)}
                                >
                                    {dbOptions.subjects.map((option) => (
                                    <MenuItem key={option.value} value={option.value}>
                                        {option.label}
                                    </MenuItem>
                                    ))}
                                </TextField>
                            </div>

                            <div className="filter-grade">
                                <TextField
                                    name="grade"
                                    className="outlined-basic"
                                    variant="outlined"
                                    margin="dense"
                                    fullWidth
                                    label="Lớp học"
                                    select
                                    value={this.state.grade}
                                    onChange={this.handleChangeGrade.bind(this)}
                                >
                                    {dbOptions.grades.map((option) => (
                                    <MenuItem key={option.value} value={option.value}>
                                        {option.label}
                                    </MenuItem>
                                    ))}
                                </TextField>
                            </div>

                            <div className="filter-level">
                                <TextField
                                    name="level"
                                    label="Cấp học"
                                    className="outlined-basic"
                                    variant="outlined"
                                    margin="dense"
                                    fullWidth
                                    select
                                    value={this.state.level}
                                    onChange={this.handleChangeLevel.bind(this)}
                                >
                                    {dbOptions.levels.map((option) => (
                                    <MenuItem key={option.value} value={option.value}>
                                        {option.label}
                                    </MenuItem>
                                    ))}
                                </TextField>
                            </div>
                            <div className="filter-text">
                                <TextField
                                        name="searchtext"
                                        autoFocus
                                        id="outlined-input"
                                        label="Tìm kiếm từ khóa"
                                        type="text"
                                        fullWidth
                                      
                                        onChange={(v) => this.setState({text:v.target.value.toLowerCase()}) }
                                        />
                            </div>
                            <div className="search-button">
                                <Button
                                    style={{
                                    width: "140px",
                                    marginTop: "12px",
                                    marginLeft: "20px",
                                    fontWeight: "400",
                                    background: "rgb(235, 43, 43)",
                                    color: "white",
                                    }}
                                    variant="contained"
                                    onClick={this.doSearch.bind(this)}
                                >
                                    Search
                                </Button>
                            </div>
                            
                        </div>
                    </div>
                </div>
                <div><h1>Các nguồn dữ liệu</h1></div>  
                <div className="source-element">
                    
                    <div className="element">
                        <Element title="ToanMath.com" task={this.state} web = "toanmath"></Element>
                    </div>     
                    <div className="element">
                        <Element title="ToanMath.com"  task={this.state} web = "toanmath"></Element>
                    </div>    
                    <div className="element">
                        <Element title="ToanMath.com"  task={this.state} web = "toanmath"></Element>
                    </div>   
                    <div className="element">
                        <Element title="ToanMath.com"  task={this.state} web = "toanmath"></Element>
                    </div>   
                    <div className="element">
                        <Element title="ToanMath.com"  task={this.state} web = "toanmath"></Element>
                    </div>   
                    <div className="element">
                        <Element title="ToanMath.com"  task={this.state} web = "toanmath"></Element>
                    </div>   
                </div>             
                
                <div><h1>Tổng hợp</h1></div>         
            </div>
        )
    }
}