import Swal from 'sweetalert2'
import withReactContent from 'sweetalert2-react-content'
import { useDispatch } from 'react-redux'
import { useNavigate } from 'react-router-dom'
import { listAllFlights, listFlightsByRoute } from '../store/slices/base/flightsSlice'
import React from 'react'

function SearchFlights() {
    const navigate = useNavigate()
    const dispatch = useDispatch()
    const MySwal = withReactContent(Swal)


    const flightSearchHandler = async (e) => {
        e.preventDefault()
        const { departureAirport, arrivalAirport } = e.target.elements

        if (departureAirport.value && arrivalAirport.value) {
            await dispatch(listFlightsByRoute({departureAirport: departureAirport.value, arrivalAirport: arrivalAirport.value}))
            navigate('/flights')
        } else if (!departureAirport.value && !arrivalAirport.value) {
            await dispatch(listAllFlights())
            navigate('/flights')
        } else {
            MySwal.fire({
                icon: 'error',
                titleText:'Input Error',
                text: 'Please enter both departure and arrival airports for a route search, or leave both blank for a full list of flights.',
                timer: 6000,
                timerProgressBar: true,
            })

          }
        };

    return (
    <>
        <div className="flex flex-wrap items-center mt-32">
            <div className="w-full md:w-4/12 px-4 mr-auto ml-auto">
            <h4 className="text-3xl font-normal leading-normal mt-0 mb-8 text-blueGray-800">
                Search For Your Next Flight
            </h4>
            <form onSubmit={flightSearchHandler} className="flex flex-wrap" >
                <div className="w-1/2 mb-3 px-2">
                <label> Departure Airport</label>
                <input
                    type="text"
                    className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                    placeholder="Departure Airport"
                    name="departureAirport"
                    />
                </div>

                <div className="w-1/2 mb-3 px-2">
                <label> Arrival Airport</label>
                <input
                    type="text"
                    className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                    placeholder="Arrival Airport"
                    name="arrivalAirport"
                />
                </div>
                <div className="text-center mb-3 px-2 w-full">
                <input
                    className="bg-blueGray-800 text-white active:bg-blueGray-600 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 w-full ease-linear transition-all duration-150"
                    type="submit"
                    value="Search Flights"
                    />
                </div>
            </form>
            </div>
        </div>
    </>
    )
}

export default SearchFlights