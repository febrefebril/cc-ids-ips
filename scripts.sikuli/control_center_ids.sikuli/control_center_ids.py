from __future__ import with_statement
from sikuli.Sikuli import *
import os
imagenscc = "C:\\Users\\lupinthe-3rd\\Documents\\teste_automatico\\imagens\\control_center\\"
addImagePath(imagenscc)

class ControlCenter(object):

    def __init__(self):
        #self.appCoordinates = (0, 0, 1024, 768)
        self.caminhoControlCenter = r'"C:\Users\lupinthe-3rd\Desktop\controlcenter\AkerControlCenter2\aker_control_center2.exe"'
        self.checaProcessoControlCenter = 0
        self.controlCenterApp = 0
        self.menuEsquerdo = 0
        self.menuConfigurationChecker = 0
        self.subMenuSystemConfigurations = 0
        self.telaIdsIps = 0

    def checaFoco(self):
        if exists("menu_superior_esquerdo.png"):
            return 1
        else:
            return 0

    def entraEmFoco(self):
        click("aker_logo_icone.png")

    def fechaJanelaConfigurarionCheckerDemo(self):
        janela = find("cabecario_demo_configuration_checker.png")
        click(janela.find("botao_fechar_configuration_checker.png"))

    def minimizaJanelaIpsIdsDemo(self):
        janela = find("cabecario_demo_ips_ids.png")
        click(janela.find("botao_minimizar_ips_ids.png"))

    def checaMinimizaJanelaIpsIdsDemo(self):
        if exists("cabecario_demo_ips_ids_minimizado.png"):
            logmsg = "minimizado com sucesso"
            return 0, logmsg
        else:
            logmsg = "erro ao minimizar"
            return 1,logmsg

    def maximizaJanelaIpsIdsDemo(self):
        janela = find("cabecario_demo_ips_ids_minimizado.png")
        click(janela.find("botao_maximizar_ips_ids.png"))

    def checaMaximizaJanelaIpsIdsDemo(self):
        if exists("cabecario_demo_ips_ids.png"):
            logmsg = "maximizado com sucesso"
            return 0, logmsg
        else:
            logmsg = "erro ao maximizar"
            return 1,logmsg
    def fechaJanelaExpandidaIpsIdsDemo(self):
        janela = find("cabecario_demo_ips_ids.png")
        click(janela.find("botao_fechar_ips_ids.png"))

    def checaFechaJanelaExpandidaIpsIdsDemo(self):
        if exists("cabecario_demo_ips_ids.png"):
            logmsg = "janela ids ips nao foi fechada"
            print logmsg
            return 1, logmsg
        else:
            logmsg = "janela ids ips fechada com sucesso"
            print logmsg
            return 0, logmsg

        
    def iniciarControlCenter(self):
        self.controlCenterApp = App("Aker Control Center")
        if not self.controlCenterApp.window():
            App.open(self.caminhoControlCenter); wait(2)
        #self.controlCenterApp.focus()
        if self.checaFoco() == 0:
            self.entraEmFoco()

    def checaIniciarControlCenter(self):
        # check application
        self.controlCenterApp.focus()
        if exists("menu_superior_esquerdo.png"):
            logmsg = "Control center foi executada com sucesso"
            print logmsg
            return 0, logmsg
        else:
            logmsg = "Control center não foi executada"
            print logmsg
            return 1, logmsg

    def minimizaSystemConfigurations(self):
        janela = find("system_configuration_expandido.png")
        click(janela.find("minimizar_system_configurations.png"))

    def checaMinimizaSystemConfigurations(self):
        if exists("system_configuration_expandido.png"):
            logmsg = "erro ao minimizar system configurations"
            print logmsg
            return 1, logmsg
        else:
            logmsg = "systemn configuration minimizado com sucesso"
            print logmsg
            return 0, logmsg

 
    def minimizaTools(self):
        janela = find("menu_esquerdo_tools_expandido.png")
        click(janela.find("minimizar_system_configurations.png"))

    def checaMinimizaTools(self):
        if exists("menu_esquerdo_tools_expandido.png"):
            logmsg = "erro ao minimizar tools"
            print logmsg
            return 1, logmsg
        else:
            logmsg = "Tools minimizado com sucesso"
            print logmsg
            return 0, logmsg

    def verificaExistenciaControlCenter():
        pass
        
    def conectaAkDemo67(self):
        self.menuEsquerdo = find("menu_medio_esquerdo.png") 
        doubleClick(self.menuEsquerdo.find("menu_medio_esquerdo_demo_fw.png"))

    def checaConectaAkDemo67(self):
        self.menuEsquerdo = find("menu_medio_esquerdo_demo_fw_expandido.png")
        #self.menuConfigurationChecker = find("menu_configuration_checker.png")
        if self.menuEsquerdo.inside().exists("menu_demo_expandido.png"):
            logmsg = "conectado ao demo do fireall 6.7 com sucesso"
            print logmsg
            return 0, logmsg
        else:
            logmsg = "Não foi possivel se conectar a demo do firewall 6.7"
            print logmsg 
            return 1, logmsg
    
    def firewall67ExpandeMenuSystemConfigurations(self):
        self.menuEsquerdo = find("menu_medio_esquerdo_demo_fw_expandido.png")
        self.menuEsquerdo.inside().doubleClick("menu_medio_esquerdo_ak67_system_conf.png")
        self.subMenuSystemConfigurations = find("fw67_sub_menu_system_configurations.png")
        self.subMenuSystemConfigurations.inside().doubleClick("intem_ips_ids.png")

    def checaFirewall67ExpandeMenuSystemConfigurations(self):
        self.telaIdsIps = find("tela_ids_ips.png")

    def maximizaSecurity(self):
        janela = find("menu_medio_esquerdo_ak67_security.png")
        click(janela.find("botao_expandir.png"))

    def checaMaximizaSecurity(self):
        if exists("menu_esquerdo_security_expandido.png"):
            logmsg = "menu security expandido com sucesso"
            print logmsg
            return 0, logmsg
        else:
            logmsg = "Erro ao tentar expandir menu security"
            print logmsg
            return 1, logmsg
   
    def entraIdsIps(self):
        janela = find("menu_esquerdo_security_expandido.png")
        doubleClick(janela.find("item_ips_ids.png"))

    def checaEntraIdsIps(self):
        if exists("tela_security_ids_ips.png"):
            logmsg = "Entrou na tela de ids ips com sucesso"
            print logmsg
            return 0, logmsg
        else:
            logmsg = "Erro ao tentar encontrar a tela ids ips"
            print logmsg
            return 1, logmsg

    def minimizaTelaSecurityIdsIps(self):
        janela = find("cabecario_demo_security_ids_ips.png")
        click(janela.find("botao_minimizar_generico.png"))

    def checaMinimizaTelaSecurityIdsIps(self):
        if exists("janela_security_minimizada.png"):
            logmsg = "janela minimizada com sucesso"
            return 0, logmsg
        else:
            logmsg = "erro ao minimizar janela demo-sucutiry-ips-ids"
            return 1, logmsg

    def maximizaTelaSecurityIdsIps(self):
        janela = find("janela_security_minimizada.png")
        click(janela.find("botao_expandir_generico.png"))

    def checaMaximizaTelaSecurityIdsIps(self):
        if exists("tela_security_ids_ips.png"):
            logmsg = "Maximizado ids ips com sucesso"
            print logmsg
            return 0, logmsg
        else:
            logmsg = "Erro ao tentar maximizar tela minimizada demo-security-ips-ids"
            print logmsg
            return 1, logmsg

    def fechaTelaSecurityIdsIps(self):
        janela = find("cabecario_demo_security_ids_ips.png")
        click(janela.find("boatao_fechar_generico.png"))

    def checaFechaTelaSecurityIdsIps(self):
        if exists("tela_security_ids_ips.png"):
            logmsg = "erro ao fechar janela demo-security-ids-ips"
            return 1,logmsg
        else:
            logmsg = "janela fechada com sucesso"
            return 0,logmsg

    def minimizaSecurity(self):
        janela = find("demo_security_expandido_ips_ids_selecionado.png")
        click(janela.find("botao_contrair_generico.png"))

    def checaMinimizaSecurity(self):
        if exists("demo_security_expandido_ips_ids_selecionado.png"):
            logmsg = "Erro ao minimizar menu demo-security-ids-ips"
            return 1,logmsg
        else:
            logmsg = "Janela demo-security-ids-ips fechada com sucesso"
            return 0,logmsg

    def expandeFw67DemoAplication(self):
        janela = find("menu_esquerdo_demo.png")
        doubleClick(janela.find("submenu_aplication.png"))

    def checaExpandeFw67DemoAplication(self):
        if exists("menu_esquer_aplication_expandido.png"):
            logmsg = "menu expandido demo-aplication expandido com sucesso"
            return 0, logmsg
        else:
            logmsg = "erro ao expandido demo-aplication"
            return 1, logmsg

    def abreAplicationDpi(self):
        janela = find("menu_esquer_aplication_expandido.png")
        doubleClick(janela.find("item_dpi.png"))

    def checaAbreAplicationDpi(self):
        if exists("tela_dpi.png"):
            logmsg = "Tela fw67-demo-aplication-dpi aberta com sucesso"
            return 0,logmsg
        else:
            logmsg = "Erro ao abrir fw67-demo-aplication-dpi"
            return 1,logmsg

    def minimizaFw67DemoAplicationDpi(self):
        #janela = find("cabecario_demo_aplication_dpi.png")
        #click(janela.find("botao_minimizar_generico.png"))
        self.encontreEClick("cabecario_demo_aplication_dpi.png", "botao_minimizar_generico.png")

    def checaMinimizaFw67DemoAplicationDpi(self):
        if exists("cabecario_demo_aplication_dpi_minimizado.png"):
            logmsg = "tela fw67-demo-aplication-dpi minimizada com sucesso"
            return 0,logmsg
        else:
            logmsg = "erro ao minimizar tela fw67-demo-aplication-dpi"
            return 1,logmsg

    def maximizaFw67DemoAplicationDpi(self):
        #janela = find("cabecario_demo_aplication_dpi_minimizado.png")
        #click(janela.find("botao_expandir_generico.png"))
        self.encontreEClick("cabecario_demo_aplication_dpi_minimizado.png", "botao_expandir_generico.png")

    def checaMaximizarFw67DemoAplicationDpi(self):
        if exists("tela_dpi.png"):
            logmsg = "Tela fw67-demo-aplication-dpi expandida com sucesso"
            return 0,logmsg
        else:
            logmsg = "Erro ao expandir fw67-demo-aplication-dpi"
            return 1,logmsg

    def encontreEClick(self, imagemCompleta, objetoClicar):
        janela = find(imagemCompleta)
        click(janela.find(objetoClicar))


        

if __name__ == "__main__":
    setShowActions(True)
    cc = ControlCenter()
    cc.iniciarControlCenter()
    cc.checaIniciarControlCenter()
    cc.conectaAkDemo67()
    cc.checaConectaAkDemo67()
    cc.fechaJanelaConfigurarionCheckerDemo()
    cc.firewall67ExpandeMenuSystemConfigurations()
    cc.checaFirewall67ExpandeMenuSystemConfigurations()
    cc.minimizaJanelaIpsIdsDemo()
    print cc.checaMinimizaJanelaIpsIdsDemo()
    cc.maximizaJanelaIpsIdsDemo()
    print cc.checaMaximizaJanelaIpsIdsDemo()
    cc.fechaJanelaExpandidaIpsIdsDemo();wait(2)
    print cc.checaFechaJanelaExpandidaIpsIdsDemo()
    cc.minimizaSystemConfigurations()
    print cc.checaMinimizaSystemConfigurations()
    cc.minimizaTools()
    print cc.checaMinimizaTools()
    cc.maximizaSecurity()
    print cc.checaMaximizaSecurity()
    cc.entraIdsIps()
    print cc.checaEntraIdsIps()
    cc.minimizaTelaSecurityIdsIps()
    print cc.checaMinimizaTelaSecurityIdsIps()
    cc.maximizaTelaSecurityIdsIps()
    print cc.checaMaximizaTelaSecurityIdsIps()
    cc.fechaTelaSecurityIdsIps()
    print cc.checaFechaTelaSecurityIdsIps()
    cc.minimizaSecurity()
    print cc.checaMinimizaSecurity()
    cc.expandeFw67DemoAplication()
    print cc.checaExpandeFw67DemoAplication()
    cc.abreAplicationDpi()
    print cc.checaAbreAplicationDpi()
    cc.minimizaFw67DemoAplicationDpi()
    print cc.checaMinimizaFw67DemoAplicationDpi()
    cc.maximizaFw67DemoAplicationDpi();wait(2)
    print cc.checaMaximizarFw67DemoAplicationDpi()
    


    exit()