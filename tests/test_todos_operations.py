from selene import browser, be, by, command

import os

def test_registration_form(browser_options):
    browser.open('/automation-practice-form')
    browser.element('#firstName').should(be.blank).type('vlad')
    browser.element('#lastName').should(be.blank).type('biryukov')
    browser.element('#userEmail').should(be.blank).type('123@gmail.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type('123455432')
    browser.element('[id="dateOfBirthInput"]').perform(command.js.scroll_into_view).click()
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__month-select').click().element(by.text('January')).click()
    browser.element('.react-datepicker__year-select').click().element(by.text('2001')).click()
    browser.element('body').click()
    browser.element('#subjectsInput').should(be.blank).type('matesha, fizra')
    browser.element('[for="hobbies-checkbox-1"]').click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('../test-pic/test_kartinka.jpg'))
    browser.element('#currentAddress').should(be.blank).type('pushkina 1')
    browser.element('#state').click().element(by.text('NCR')).click()
    browser.element('#city').click().element(by.text('Delhi')).click()
    browser.element('#submit').click()





