import { EventEmitter } from 'events';
import dispatcher from '../dispatcher';

export class UserStore extends EventEmitter{
    constructor(){
        super();
        this.auth = {
            isAuthenticated : false,
            jwt : null
        }
    }

    isLoggedIn(){
        return this.auth.isAuthenticated;
    }

    getJwt(){
        return this.auth.jwt;
    }

    loginUser(token){
        this.auth.isAuthenticated = true;
        this.emit('change');
    }
    logout(){
        this.auth.isAuthenticated = false;
        //delete token
        console.log('emitting logout');
        this.emit('change');
    }

    handleActions(action){
        switch (action.type) {
            case "LOGIN_USER":
                this.loginUser(action.jwt);
                break;
            case "LOGOUT_USER":
                console.log('handling logout');
                this.logout();
                break
        }
    }
   

}

const userStore = new UserStore;
dispatcher.register(userStore.handleActions.bind(userStore));
export default userStore;
