import { Fragment } from 'react'
import { Menu, Transition } from '@headlessui/react'
import { NavLink } from 'react-router-dom'

function classNames(...classes) {
  return classes.filter(Boolean).join(' ')
}

export default function RegisterDropDown() {
  return (
    <Menu as="div" className="relative inline-block text-left">
      <div>
        <Menu.Button className="bg-sky-500 text-white active:bg-sky-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150">
        <i className="fas fa-user-plus px-2"></i>Register<i className="fas fa-chevron-down px-2"></i>
        </Menu.Button>
      </div>

      <Transition
        as={Fragment}
        enter="transition ease-out duration-100"
        enterFrom="transform opacity-0 scale-95"
        enterTo="transform opacity-100 scale-100"
        leave="transition ease-in duration-75"
        leaveFrom="transform opacity-100 scale-100"
        leaveTo="transform opacity-0 scale-95"
      >
        <Menu.Items className="absolute right-0 z-10 mt-2 w-56 origin-top-right rounded bg-sky-500 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none text-white active:bg-sky-600 font-bold uppercase text-xs hover:shadow-md outline-none mr-1 mb-1 ease-linear transition-all duration-150">
          <div className="py-1">
            <Menu.Item>
              {({ active }) => (
                <NavLink
                  to = '/register-customer'
                  className={classNames(
                    active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                    'block px-4 py-2 text-sm'
                  )}
                >
                  Customer
                </NavLink>
              )}
            </Menu.Item>
            <hr/>
            <Menu.Item>
              {({ active }) => (
                <NavLink
                  to = '/register-airline'
                  className={classNames(
                    active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                    'block px-4 py-2 text-sm'
                  )}
                >
                  Airline
                </NavLink>
              )}
            </Menu.Item>
          </div>
        </Menu.Items>
      </Transition>
    </Menu>
  )
}
