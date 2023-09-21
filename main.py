from selenium import webdriver
from selenium.webdriver.common.by import By


def testing_the_sparks_foundation_website():
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    browser.get("https://www.thesparksfoundationsingapore.org/")

    # checking if the logo image is displayed
    try:
        logo_image = browser.find_element(By.CLASS_NAME, "top-header-agile")
        assert logo_image.is_displayed()
        print("Logo image displayed? True")
    except:
        print("Logo image displayed? False")

    # checking if the navbar appers
    try:
        navbar = browser.find_element(By.CLASS_NAME, "navbar")
        assert navbar.is_displayed()
        print("Navbar appeared? True")
    except:
        print("Navbar appeared? False")

    # check if the The Sparks Foundation video appears
    try:
        video = browser.find_element(By.ID, "youtube-video")
        assert video.is_displayed()
        print("Video appeared? True")
    except:
        print("Video appeared? False")

    # check if professional courses icon appears
    try:
        professional_courses_icon = browser.find_element(
            By.CLASS_NAME, "fa-graduation-cap"
        )
        assert professional_courses_icon.is_displayed()
        print("Professional Courses Icon appeared? True")
    except:
        print("Professional Courses Icon appeared? False")

    # check if the learn more button appears
    try:
        learn_more_button = browser.find_element(By.CLASS_NAME, "hvr-rectangle-out")
        learn_more_button.is_displayed()
        print("Learn More Button appeared? True")
    except:
        print("Learn More Button appeared? False")

    # check if the footer appears
    try:
        footer = browser.find_element(By.CLASS_NAME, "footer")
        assert footer.is_displayed()
        print("Footer appeared? True")
    except:
        print("Footer appeared? False")

    # checking if the contact us page is displayed
    try:
        contact_us_page_expected_url = (
            "https://www.thesparksfoundationsingapore.org/contact-us/"
        )
        contact_us_page = browser.find_element(By.LINK_TEXT, "Contact Us")
        contact_us_page.click()

        # checking for succesfull navigation
        assert browser.current_url == contact_us_page_expected_url
        print("Contact Us page displayed? True")
    except:
        print("Contact Us page displayed? False")

    # checking if the location marker on the contact page is dsiplayed
    try:
        location_marker = browser.find_element(By.CLASS_NAME, "fa-map-marker")
        assert location_marker.is_displayed()
        print("Location marker displayed? True")
    except:
        print("Location marker displayed? False")

    # navigate back to home page and check student scholarship page
    browser.back()
    print("Home page displayed? True")
    try:
        student_scholarship_page_expected_url = "https://www.thesparksfoundationsingapore.org/programs/student-scholarship-program/"
        student_scholarship_page = browser.find_element(
            By.LINK_TEXT, "Student Scholarship Program"
        )
        student_scholarship_page.click()
        assert browser.current_url == student_scholarship_page_expected_url
        print("Student Scholarship Page displayed? True")

    except:
        print("Student Scholarship Page displayed? False")

    # checking if the topic line on student scholarship page is correct
    try:
        topic_line = browser.find_element(By.CLASS_NAME, "para-w3-agile")
        assert (
            topic_line.text
            == "Money is not the only answer, but it makes a difference."
        )
        print("Topic line on Student Scholarship Page correct? True")
    except:
        print("Topic line on Student Scholarship Page correct? False")

    # navigate back to home page and check student mentorship program page
    browser.back()
    try:
        student_mentorship_page_expected_url = "https://www.thesparksfoundationsingapore.org/programs/student-mentorship-program/"
        student_mentorship_page = browser.find_element(
            By.LINK_TEXT, "Student Mentorship Program"
        )
        student_mentorship_page.click()
        assert browser.current_url == student_mentorship_page_expected_url
        print("Student Mentorship Page displayed? True")

    except:
        print("Student Mentorship Page displayed? False")

    # checking if the topic line on student mentorship page is dsiplayed
    try:
        topic_line = browser.find_element(By.CLASS_NAME, "para-w3-agile")
        assert (
            topic_line.text
            == "Don't limit a child to your own learning, for he was born in another time."
        )
        print("Topic line on Student Mentorship Page correct? True")
    except:
        print("Topic line on Student Mentorship Page correct? False")

    # navigate back to the home page and check student sos program page
    browser.back()
    try:
        student_sos_program_page_expected_url = (
            "https://www.thesparksfoundationsingapore.org/programs/student-sos-program/"
        )
        student_sos_program_page = browser.find_element(
            By.LINK_TEXT, "Student SOS Program"
        )
        student_sos_program_page.click()
        assert browser.current_url == student_sos_program_page_expected_url
        print("Student SOS Program Page displayed? True")

    except:
        print("Student SOS Program Page displayed? False")

    # check if the main title on student sos program page is correct
    try:
        main_title_on_sos_page = browser.find_element(
            By.CLASS_NAME, "inner-tittle-w3layouts"
        )
        assert main_title_on_sos_page.text == "Student SOS Program"
        print("Main title on Student SOS Page correct? True")
    except:
        print("Main title on Student SOS Page correct? False")

    browser.quit()


testing_the_sparks_foundation_website()
