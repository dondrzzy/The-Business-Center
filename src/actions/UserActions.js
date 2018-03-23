import dispatcher from "../dispatcher";
// import axios from "axios";

export const authenticate_user = (email, password) =>{
    dispatcher.dispatch({
        type:"LOGIN_USER",
        jwt:'0019'
    });
}

export const logout = () =>{
    dispatcher.dispatch({
        type:"LOGOUT_USER"
    });
}

export const updateTodo = id =>{
    dispatcher.dispatch({
        type:"UPDATE_TODO",
        id
    });
}

// export const getBusinesses = () =>{     
//     dispatcher.dispatch({ type:"FETCHING_BUSINESSES" });
//     axios.get("http://127.0.0.1:5000/api/v1/businesses")
//         .then(res => {
//             console.log('fetched', res.data);
//             dispatcher.dispatch({
//                 type:"LOAD_BUSINESSES",
//                 data:res.data
//             })
//         })
         
// }