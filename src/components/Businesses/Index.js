import React, {Component} from 'react';
import BusinessItem from './BusinessItem';

export default class Businesses extends Component{
    render(){
        console.log(this.props);
        return(
            <div className="businesses">
                <div className="row">
                    <div className="col-md-12">
                        <div className="jumbotron">
                            <h4>Business</h4>
                            <p>We at Business are tailored to suit your needs. Filter through business by location or category</p>                
                            <div className="row">
                                <div className="col-md-6 ">
                                    <form action="" metho="post">
                                        <div className="form-group">
                                            <label htmlFor="searchstr" className="control-label">Search:</label>
                                            <input type="text" name="searchstr" className="form-control" value="" placeholder="*Type company name..." />
                                        </div>
                                        <div className="form-group">
                                            <label className="control-label" htmlFor="">Filter By Cartegory:</label>
                                            <select name="cat" id="" className="form-control">
                                                <option ></option>
                                            </select>
                                        </div>
                                        <div className="form-group">
                                            <label className="control-label" htmlFor="">Filter By Location:</label>
                                            <select name="location" id="" className="form-control">
                                                <option ></option>
                                            </select>
                                        </div>
                                        <button className="btn btn-primary btn-block btn-md">SEARCH</button>
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div className="row">
		            <div className="col-md-12">
                        <BusinessItem />
                    </div>
                </div>
            </div>
        )
    }
}
