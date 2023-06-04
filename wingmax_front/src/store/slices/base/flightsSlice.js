import { createSlice } from '@reduxjs/toolkit';
import axios from 'axios';


const initialState = { flights: null, loading: false, error: null };

const flightsSlice = createSlice({
    name: 'flights',
    initialState,
    reducers: {
        flightsRequest: (state, action) => {         
            state.loading = true;
        },
        flightsSuccess: (state, action) => {
            state.loading = false;
            state.flights = action.payload;
        },
        flightsFail: (state, action) => {
            state.loading = false;
            state.error = action.payload;
        }
    } 
});

export const { flightsRequest, flightsSuccess, flightsFail } = flightsSlice.actions;
export default flightsSlice.reducer;

export const listAllFlights = (page = 1) => async (dispatch) => {
    try{
        dispatch(flightsRequest());
        const response = await axios.get('/api/flights?page=${page}');
        dispatch(flightsSuccess(response.data));
    } catch (error) {
        const message = error.response && error.response.data.message ? error.response.data.message : error.message;
        dispatch(flightsFail(message));
    }
}

export const listFlightsByRoute = (departureAirport, arrivalAirport, page = 1) => async (dispatch) => {
    try{
        dispatch(flightsRequest());
        const response = await axios.get('/api/flights/${departureAirport}/${arrivalAirport}?page=${page}');
        dispatch(flightsSuccess(response.data));
    } catch (error) {
        const message = error.response && error.response.data.message ? error.response.data.message : error.message;
        dispatch(flightsFail(message));
    }
}

