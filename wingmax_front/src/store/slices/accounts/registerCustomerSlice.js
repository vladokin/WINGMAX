import { createSlice } from '@reduxjs/toolkit';
import axios from 'axios';


const initialState = { loading: false, error: null };

const registerCustomerSlice = createSlice({
    name: 'registerCustomer',
    initialState,
    reducers: {
        registerCustomerRequest: (state, action) => {
            state.loading = true;
        },
        registerCustomerSuccess: (state, action) => {
            state.loading = false;
        },
        registerCustomerFail: (state, action) => {
            state.loading = false;
            state.error = action.payload;
        }
    }
});

export const { registerCustomerRequest, registerCustomerSuccess, registerCustomerFail } = registerCustomerSlice.actions;
export default registerCustomerSlice.reducer;

export const registerCustomer = (firstName,lastName, username, email, password1, password2) => async (dispatch) => {
        try{
            dispatch(registerCustomerRequest());
            const response = await axios.post('/api/users/register-customer', { firstName,lastName, username, email, password1, password2 }, { headers: { 'Content-Type': 'application/json' } });
            dispatch(registerCustomerSuccess(response.data));
        } catch (error) {
            const message = error.response && error.response.data.message ? error.response.data.message : error.message;
            dispatch(registerCustomerFail(message));
        }
    };
