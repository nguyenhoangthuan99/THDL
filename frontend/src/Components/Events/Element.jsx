import React from "react";
import "./index.css";
import Image from "../../Base/Image.jsx"
import {events} from "../../dummydb/dbEvents"
import api from "../../Base/fetchData"
import ViewMore from "../Common/ViewMore";
export default class Element extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            title:this.props.title,
            task:this.props.task,
            web:this.props.web,
            list: [],
            activeIndex:null,
            page:1,
            loading:false
        }
        
    };
    componentDidMount(){
        console.log("start mount")
        this.Search();
    }
    seeMore(){
        this.setState({page:this.state.page+1});
        this.SearchMore();
    };
    async Search(){
        var task_id = this.props.task[this.props.web];
        console.log("task id",task_id)
        this.setState({loading:true})
        var result= await api.getResult(task_id);
        this.setState({list:[...this.state.list,...result]})
        this.setState({loading:false})
    }
    async SearchMore(){
        this.setState({loading:true})
        var body = {
            "type": this.props.type,
            "subject": this.props.subject,
            "grade": this.props.grade,
            "level": this.props.level,
            "text": this.props.text,
            "page": this.state.page
        }
        var result= await api.searchOneWeb(body,this.state.web);
        this.setState({list:[...this.state.list,...result]})
        this.setState({loading:false})
    }
    render(){
        let viewMoreActive = this.state.list.length > this.state.limit;
        return(
            <div className="wrapper-items">
                <div><h2>{this.state.title}</h2></div>
                <div className="eventsItems">
                
                    {
                        this.state.list.slice(0,this.state.limit).map((item,index) => (   
                                
                            <a href={item.link} target="_blank">
                                <div key={index} className="eventsItem">
                                    <div className="eventsDate">
                                    <img src={Image.vsdx}></img>
                                    </div>
                                    <div className="eventsContent">
                                    <div className="eventsItemTitle"> {item.title}</div>
                                    <div className="eventsItemTime">
                                        <img className="eventsIcon" src={Image.clock}/>
                                        <div className="eventsItemStartEnd">{item.date}</div>
                                    </div>
                                    </div>
                                </div>
                            </a>
                    ))
                    }
                    
                </div>
                <div className="view-more">{viewMoreActive &&
                        <ViewMore  className="viewmore"  onClick={this.seeMore.bind(this)}/> }
                    </div>
            </div>
        )
    }
}