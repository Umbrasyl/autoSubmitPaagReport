from selenium import webdriver
from selenium.webdriver.common.by import By
from fillPatientRecords import fillPatientRecords
import time


def main():
    
    driver = webdriver.Chrome()
    driver.get("https://tb.saglik.gov.tr/")
    
    login_link = driver.find_element(By.XPATH, '//a[@href="/Account/SSOLogin?SSO=true"]')
    login_link.click()
    
    e_signature_button = driver.find_element(By.XPATH, '//p[text()="e-İmza"]')
    e_signature_button.click()
    time.sleep(4)
    
    use_button = driver.find_element(By.XPATH, '//a[text()="kullan"]')
    use_button.click()
    
    password_input = driver.find_element(By.XPATH, '//input[@id="password_1"]')
    password_input.send_keys("123321")
    
    login_button = driver.find_element(By.XPATH, '//button[@id="btnImzala"]')
    login_button.click()
    time.sleep(7)
    
    organization_choice = driver.find_element(By.XPATH, '//*[@id="kurumListesi"]/div[2]/button')
    organization_choice.click()
    time.sleep(2)
    
    module_choice = driver.find_element(By.XPATH, '//button[contains(text(), "Tüberküloz")]')
    module_choice.click()
    time.sleep(4)
    
    patient_records = driver.find_element(By.XPATH, '//a[@href="/Tuberkuloz/Islem/HastaSorgu"]')
    patient_records.click()
    time.sleep(4)
    
    is_draft_select = driver.find_element(By.XPATH, '//*[@id="TaslakMi"]')
    is_draft_select.click()
    time.sleep(1)
    
    yes_draft = driver.find_element(By.XPATH, '//*[@id="TaslakMi"]/option[@value="true"]')
    yes_draft.click()
    
    cause_of_examination = driver.find_element(By.XPATH, '//select[@id="BasvuruNedeni"]')
    cause_of_examination.click()
    time.sleep(1)
    
    cause_of_examination_choice = driver.find_element(By.XPATH, '//*[@id="BasvuruNedeni"]/option[@value="9"]')
    cause_of_examination_choice.click()
    
    search_button = driver.find_element(By.XPATH, '//input[@id="btnGridYenile"]')
    search_button.click()
    time.sleep(4)
    
    list_length_choice = driver.find_element(By.XPATH, '//select[@name="gridHastaSorgulama_length"]')
    list_length_choice.click()
    
    list_length_choice_100 = driver.find_element(By.XPATH, '//option[@value="100"]')
    list_length_choice_100.click()
    time.sleep(4)
    
    # Get all the patient links
    patients = driver.find_elements(By.XPATH, '//a[contains(text(), "Hasta Muayene(Taslak) ")]')
    
    count = 0
    # Loop for each patient
    while len(patients) > 0:
        count += 1
        fillPatientRecords(driver, patients[0])
        time.sleep(4)
        search_button = driver.find_element(By.XPATH, '//input[@id="btnGridYenile"]')
        search_button.click()
        time.sleep(4)
        patients = driver.find_elements(By.XPATH, '//a[contains(text(), "Hasta Muayene(Taslak) ")]')
        
    print(f"{count} hasta dosyası 'Aktif Spesifik Lezyon yok' olarak kapatıldı...")


main()