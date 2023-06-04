import { configureStore } from '@reduxjs/toolkit';
import loginReducer from './slices/accounts/loginSlice'
import registerCustomerReducer from './slices/accounts/registerCustomerSlice';
import registerAirlineReducer from './slices/accounts/registerAirlineSlice';
import flightsReducer from './slices/base/flightsSlice';


const store = configureStore({
    reducer: {
        login: loginReducer,
        registerCustomer: registerCustomerReducer,
        registerAirline: registerAirlineReducer,
        flights: flightsReducer,
    },
});


export default store;