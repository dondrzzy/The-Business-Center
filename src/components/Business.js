import React, {Component} from 'react';
import { Link } from 'react-router-dom';

export default class Business extends Component{
    render(){
        return(
            <div className="business-item">
                <div className="row">
                    <div className="col-md-12">
                        <div className="jumbotron">
                            <h3>Business | <span>Category</span></h3>
                            <p>We at Business are tailored to suit your needs</p>   
                            <hr />     
                            <button data-toggle="modal" data-target="#myModal" className="btn btn-primary btn-sm">
                                Update Business
                            </button>        
                            <Link to="#" id="edit_b" className="btn btn-danger btn-sm">Delete</Link>        
                        </div>                        
                    </div>
                </div>
                <hr />
                <div className="row">
                    <div className="col-md-12">
                        <h4>Description</h4>
                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illum quam ad nam molestiae. Qui tempore, laudantium ex. Quaerat unde aperiam quo, voluptatibus adipisci. Laudantium ut delectus cumque voluptatem minima blanditiis.</p>
                    </div>
                </div>
                <div className="row">
                    <div className="col">
                        <div className="card border-light mb-3">
                            <div className="card-header">Our Services</div>
                            <div className="card-body">
                                <h6>Perferendis</h6>
                                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Facilis, aut at et, ratione id debitis, necessitatibus iure repellendus eveniet explicabo labore perferendis! Maiores nobis minima error impedit ab officia amet?</p>
                                <hr/>
                                <h6>Impedit ab Officia</h6>
                                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Facilis, aut at et, ratione id debitis, necessitatibus iure repellendus eveniet explicabo labore perferendis! Maiores nobis minima error impedit ab officia amet?</p>
                                <hr/>
                                <h6>Ratione id Debitis</h6>
                                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Facilis, aut at et, ratione id debitis, necessitatibus iure repellendus eveniet explicabo labore perferendis! Maiores nobis minima error impedit ab officia amet?</p>
                                <hr />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}
