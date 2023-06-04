import { createSlice } from '@reduxjs/toolkit';
import axios from 'axios';

const initialState = { loading: false, error: null };

const registerAirlineSlice = createSlice({
    name: 'registerAirline',
    initialState,
    reducers: {
        registerAirlineRequest: (state, action) => {
            state.loading = true;
        },
        registerAirlineSuccess: (state, action) => {
            state.loading = false;
        },
        registerAirlineFail: (state, action) => {
            state.loading = false;
            state.error = action.payload;
        }
    }
});

export const { registerAirlineRequest, registerAirlineSuccess, registerAirlineFail } = registerAirlineSlice.actions;
export default registerAirlineSlice.reducer;

export const registerAirline = (iataCode, name, username, email, password1, password2) => async (dispatch) => {
    try{
        dispatch(registerAirlineRequest());
        const response = await axios.post('/api/users/register-airline', { iataCode, name, username, email, password1, password2 }, { headers: { 'Content-Type': 'application/json' } });
        dispatch(registerAirlineSuccess(response.data));
    } catch (error) {
        const message = error.response && error.response.data.message ? error.response.data.message : error.message;
        dispatch(registerAirlineFail(message));
    }
};
