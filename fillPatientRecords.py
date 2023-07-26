from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time


def fillPatientRecords(driver, patient_link):
    patient_link.click()
    time.sleep(3)

    patient_anamnesis_button = driver.find_element(By.XPATH, '//a[@id="btnLinkAnamnez"]')
    patient_anamnesis_button.click()
    time.sleep(3)

    relative_with_tb_radio = driver.find_element(By.XPATH, '//input[@id="YakinlarindaTBliVarMi" and @value="Bilinmiyor"]')
    relative_with_tb_radio.click()

    ex_tb_treatment_radio = driver.find_element(By.XPATH, '//input[@id="DahaOnceTuberkuloz" and @value="Bilinmiyor"]')
    ex_tb_treatment_radio.click()

    pregnant_select = driver.find_elements(By.XPATH, '//select[@id="GebeMi"]')
    if len(pregnant_select) > 0:
        pregnant_select[0].click()
        pregnant_choice = driver.find_element(By.XPATH, '//option[@value="2" and text()="Gebe Değil"]')
        pregnant_choice.click()

    patient_anamnesis_save_button = driver.find_element(By.XPATH, '//button[@id="KaydetButtonClick"]')
    patient_anamnesis_save_button.click()
    time.sleep(4)
    
    ActionChains(driver).send_keys(Keys.PAGE_UP).perform()
    time.sleep(2)
    
    patient_examination_button = driver.find_element(By.XPATH, '//*[@id="btnLinkMuayene"]')
    patient_examination_button.click()
    time.sleep(4)

    patient_tests_button = driver.find_element(By.XPATH, '//a[@id="btnLinkTetkik"]')
    patient_tests_button.click()
    time.sleep(4)

    add_internal_test = driver.find_element(By.XPATH, '//a[@id="icTetkikEkle"]')
    add_internal_test.click()
    time.sleep(4)

    test_paag_input = driver.find_element(By.XPATH, '//*[@id="RadyolojiGrafiVM_PaAkcigerGrafisiTekYon"]')
    test_paag_input.click()

    save_test_choice = driver.find_element(By.XPATH, '//button[@id="btnSave" and @value="Radyoloji Tetkik Kaydet"]')
    save_test_choice.click()
    time.sleep(1)

    dismiss_modal_button = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div/div[2]/section/div/article/div/div/div/form/div[2]/div/div/button[1]')
    dismiss_modal_button.click()
    time.sleep(1)

    enter_test_result = driver.find_element(By.XPATH, '//*[@id="IcTetkikGrid"]/tbody/tr/td[8]/div/button')
    enter_test_result.click()

    test_result_select = driver.find_element(By.XPATH, '//*[@id="IcTetkikGrid"]/tbody/tr/td[8]/div/ul/li[1]/a[contains(text(), "Sonuç")]')
    test_result_select.click()
    time.sleep(3)
    
    test_result_choice_select = driver.find_element(By.XPATH, '//select[@id="CekimSonucuId"]')
    test_result_choice_select.click()

    test_result_choice = driver.find_element(By.XPATH, '//*[@id="CekimSonucuId"]/option[@value="2"]')
    test_result_choice.click()
    time.sleep(2)

    test_date_input = driver.find_element(By.XPATH, '//input[@id="CekimTarihi"]')
    test_date_input.click()
    time.sleep(2)

    test_date_choice = driver.find_element(By.XPATH, '//td[contains(@class, " ui-datepicker-days-cell-over  ui-datepicker-today")]')
    test_date_choice.click()
    time.sleep(1)

    findings_select = driver.find_element(By.XPATH, '//select[@id="TBDisTetkikSonucBulgularId"]')
    findings_select.click()

    findings_choice = driver.find_element(By.XPATH, '//option[@value="1" and text()="Aktif Spesifik Lezyon Yok"]')
    findings_choice.click()

    test_result_save_button = driver.find_element(By.XPATH, '//button[@id="btnSaveKoruma"]')
    test_result_save_button.click()
    time.sleep(1)

    close_test_result_button = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div/div[2]/section/div/article/div/div/div/form/fieldset/div[5]/div/div/button[1]')
    close_test_result_button.click()
    time.sleep(2)

    final_screen_link = driver.find_element(By.XPATH, '//a[@id="btnLinkMuayeneSonucu"]')
    final_screen_link.click()
    time.sleep(4)

    result_select = driver.find_element(By.XPATH, '//select[@id="MuayeneSonucu"]')
    result_select.click()

    result_choice = driver.find_element(By.XPATH, '//option[@value="16" and text()="Rapor Verildi"]')
    result_choice.click()

    for i in range(2):
        final_screen_save_button = driver.find_element(By.XPATH, '//button[@id="KaydetButtonClick"]')
        final_screen_save_button.click()
        time.sleep(2)
    
        confirm_button = driver.find_element(By.XPATH, '//button[@id="bot2-Msg1"]')
        confirm_button.click()
        time.sleep(2)
    
    ActionChains(driver).send_keys(Keys.PAGE_UP).perform()
    time.sleep(4)

    return_button = driver.find_element(By.XPATH, '//a[@href="/Tuberkuloz/Islem/HastaSorgu?listeyeDon=true"]')
    return_button.click()