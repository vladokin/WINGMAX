import { createSlice } from '@reduxjs/toolkit';
import axios from 'axios';

const initialState = { userInfo: null, loading: false, error: null };

const loginSlice = createSlice({
    name: 'login',
    initialState,
    reducers: {
        loginRequest: (state, action) => {
            state.loading = true;
        },
        loginSuccess: (state, action) => {
            state.loading = false;
            state.userInfo = action.payload;
        },
        loginFail: (state, action) => {
            state.loading = false;
            state.error = action.payload;
        },
        logout: (state, action) => {
            state.userInfo = null;
        }
    }
});

export const { loginRequest, loginSuccess, loginFail, logout } = loginSlice.actions;
export default loginSlice.reducer;

export const login = (email, password) => async (dispatch) => {
    try{
        dispatch(loginRequest());
        const response = await axios.post('http://127.0.0.1:8000/api/users/login/', { email, password }, { headers: { 'Content-Type': 'application/json' } });
        dispatch(loginSuccess(response.data));
        localStorage.setItem('userInfo', JSON.stringify(response.data));
    } catch (error) {
        const message = error.response && error.response.data.message ? error.response.data.message : error.message;
        dispatch(loginFail(message));
    }
};

export const logoutUser = () => (dispatch) => {
    localStorage.removeItem('userInfo');
    dispatch(logout());
}
