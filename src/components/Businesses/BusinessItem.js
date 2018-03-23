import React, {Component} from 'react';
import {Link} from 'react-router-dom';

export default class BusinessItem extends Component{
    constructor(){
        super();
        this.state = {
            formMounted : false
        }
    }

    showPostForm(){
        this.setState({formMounted:true})
    }
    hidePostForm(){
        this.setState({formMounted:false})
    }
    render(){
        let postForm;
        postForm = this.state.formMounted 
            ?<div className="form-group">
                <textarea name='comment' className='form-control'></textarea>
                <button className='btn btn-sm btn-success'>Post</button>
                <button className="btn btn-link" onClick={this.hidePostForm.bind(this)}>cancel</button>
			</div>
            : "";
        return(
            <div className="business-item">
                <div className="card border-secondary mb-3">
                    <div className="card-header">
                        <h4><Link to="businesses/1">Business Name</Link> | <span>Category</span></h4>
                    </div>
                    <div className="card-body">
                        <p>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consequatur laborum dolor non reprehenderit aliquid, expedita quidem quas doloremque magnam magni nemo minima ducimus aut hic rem neque eius! Harum, id.
                        </p>				
                        <div>
                            <p>Location: <small>Address</small></p>
                        </div>
                                
                            
                        <hr />
                        <button data-toggle="collapse" className="btn btn-sm btn-default" data-target="#reviews1" type="button"aria-expanded="false" aria-controls="reviews1">
                            Show Reviews <i className="fas fa-comment"></i>
                        </button>
                        <button type="button" className="btn btn-sm btn-primary" onClick={this.showPostForm.bind(this)}>Post Review</button>
                        {postForm}
                        <div id="reviews1" className="collapse">
                            <small>
                                <p><b>User : </b>Lorem ipsum dolor sit amet, consectetur adipisicing elit. <a href="">edit</a> | <a href="">delete</a></p>
                                <p><b>User : </b>Consequatur laborum dolor non reprehenderit aliquid, expedita quidem quas doloremque magnam</p>
                                <p><b>User : </b>magni nemo minima ducimus aut hic rem neque eius! Harum, id</p>
                            </small>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}
