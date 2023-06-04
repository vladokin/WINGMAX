import React from 'react'

function Footer() {
  return (
    <section className="pb-20 relative block bg-blueGray-800">
          <div
            className="bottom-auto top-0 left-0 right-0 w-full absolute pointer-events-none overflow-hidden -mt-20 h-20"
            style={{ transform: "translateZ(0)" }}
          >
            <svg
              className="absolute bottom-0 overflow-hidden"
              xmlns="http://www.w3.org/2000/svg"
              preserveAspectRatio="none"
              version="1.1"
              viewBox="0 0 2560 100"
              x="0"
              y="0"
            >
              <polygon
                className="text-blueGray-800 fill-current"
                points="2560 0 2560 100 0 100"
              ></polygon>
            </svg>
          </div>
          <div className="container mx-auto px-4 lg:pt-24 lg:pb-64">
            <div className="flex flex-wrap text-center justify-center">
              <div className="w-full lg:w-6/12 px-4">
                <h5 className="text-2xl font-semibold text-white">
                  Have a Nice Flight
                </h5>
                <p className="text-sm leading-relaxed mt-4 mb-4 text-blueGray-400">
                  Design Template: <a href="https://www.creative-tim.com" target="_blank" className="text-blueGray-300 hover:text-blueGray-400">Creative Tim</a>
                  <br />
                  Developer - Vlad Novichonok:
                  <br />
                  <a href="https://www.linkedin.com/in/vlad-novichonok-73171063" target="_blank" className='mr-4'><i className="fas fa-brands fa-linkedin"></i></a><a href="https://github.com/vladokin" target="_blank"><i className="fas fa-brands fa-github"></i></a>
                </p>
              </div>
            </div>
          </div>
        </section>
  )
}

export default Footer