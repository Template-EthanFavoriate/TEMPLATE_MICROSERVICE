#!/usr/bin/python
'''
	Creation-Date: 2013-08-07
	Updated-Date 2014-02-20
	Authors:
	to release:
	cd /srv/Eclipse-Wrokspace
	pip install ./keplerapp_tbmodel --upgrade
	
	employee.py
	class Employee
'''
from django.db import models
from datetime import datetime

class Employee(models.Model):
	EmpID = models.AutoField(primary_key=True,blank=True)
	OrgId = models.CharField(max_length=50, db_index=True)#PNC
	EmpLevelCode = models.IntegerField(db_index=True,blank=True,null=True)#6
	EmpName = models.CharField(max_length=100)#Gender
	EmpGender = models.CharField(max_length=50,blank=True,null=True)#F
	EmpHire_dttm = models.DateTimeField(blank=True,null=True)
	upd_dttm = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return u'System: %s'%self.EmpName
		
	class Meta:
		app_label = 'keplerapp_tbmodel'
		db_table = u'employee'

	#Return a Generic object
	@classmethod
	def get_Name_by_EmpID(cls,EmpID):
		return cls.objects.filter(EmpID=EmpID)
	
	@classmethod
	def get_Name_by_OrgID(cls,OrgId):
		return cls.objects.filter(OrgId=OrgId)

	@classmethod
	def truncate(cls):
		cls.objects.all().delete()

	@classmethod
	def prepare_data(cls):
		Employee(OrgId='2',EmpLevelCode=1,EmpName='Ethan W').save()
		Employee(OrgId='2',EmpLevelCode=1,EmpName='Clint H').save()
		Employee(OrgId='2',EmpLevelCode=2,EmpName='Brad G').save()
		Employee(OrgId='3',EmpLevelCode=1,EmpName='Larry E').save()
		Employee(OrgId='3',EmpLevelCode=2,EmpName='Larry P').save()
		
		
#	#Return list ['F','M','SELF','SPOUSE']
#	@classmethod
#	def get_ruleset_by_client(cls,NomenSourceSystem):
#		try:
#			rule_set = cls.objects.filter(NomenSourceSystem=NomenSourceSystem)
#		except Exception, e: raise Exception('ERROR at Nomenclature.get_obj_by_client. %s'%e)
#		return map(lambda x:str(x.NomenCode),rule_set)
#
#	#Return hashmap [6:['F','M'], 20:['SELF','SPOUSE']]
#	@classmethod
#	def get_ruledict_by_client(cls,NomenSourceSystem):
#		try:
#			rule_set = cls.objects.filter(NomenSourceSystem=NomenSourceSystem)
#		except Exception, e: raise Exception('ERROR at Nomenclature.get_obj_by_client. %s'%e)
#		result={}
#		for rule in rule_set:
#			if rule.NomenCSVField in result:
#				result[rule.NomenCSVField].append(str(rule.NomenCode))
#			else:
#				result[rule.NomenCSVField] = [str(rule.NomenCode)]
#		return result
#
