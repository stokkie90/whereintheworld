import React from 'react'
import GoogleMapReact from 'google-map-react'
import { MapPin } from '../components/MapPin'
import { MainOverlay } from '../components/MainOverlay'
import { TripView } from '../components/TripView'
import { tripLogic } from '../logics/tripLogic'
import { useValues } from 'kea'
import clsx from 'clsx'
import { WhoAmI } from '../components/WhoAmI'
import { TimeTravel } from '../components/TimeTravel'
import { userLogic } from '../logics/userLogic'

function Home(): JSX.Element {
    const { openTripId } = useValues(tripLogic)
    const { users } = useValues(userLogic)
    const defaultProps = {
        center: {
            lat: 51.5,
            lng: 0.0,
        },
        zoom: 1,
    }
    return (
        <div className="map-container">
            <WhoAmI />
            <MainOverlay />
            <TimeTravel />
            <div className={clsx('trip-view-wrapper', { hidden: !openTripId })}>{openTripId && <TripView />}</div>

            <GoogleMapReact
                bootstrapURLKeys={{ key: typeof window !== 'undefined' && window.location.origin === 'https://whereintheworld.posthog.com' && 'AIzaSyDOV1fvZoiOUskMxIYF8sSBNgVhoCNzxsk' }}
                defaultCenter={defaultProps.center}
                defaultZoom={defaultProps.zoom}
                fullscreenControl={false}
                options={{ fullscreenControl: false }}
            >
                {users.map((user) => (
                    <MapPin
                        lat={user.location.latitude}
                        lng={user.location.longitude}
                        avatarUrl={(user.avatar || '').replace('_1024.', '_72.')} // try loading a smaller image if from slack
                        travelState={user.location.isHome ? 'home' : 'away'}
                        key={user.id}
                    />
                ))}
            </GoogleMapReact>
        </div>
    )
}

export default Home