package com.chaboshi.www.controllers.wap;

import java.util.Enumeration;
import java.util.List;
import java.util.Map;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.alibaba.fastjson.JSONObject;
import com.chaboshi.crpc.commonservice.entity.Banner;
import com.chaboshi.crpc.commonservice.entity.OrderSource;
import com.chaboshi.scf.userservice.entity.UserDetail;
import com.chaboshi.wf.mvc.ActionResult;
import com.chaboshi.wf.mvc.action.MethodActionResult;
import com.chaboshi.wf.mvc.annotation.Path;
import com.chaboshi.www.controllers.web.BaseController;
import com.chaboshi.www.inits.ServiceInit;
import com.chaboshi.www.interceptors.SourceValidate;
import com.chaboshi.www.service.IBannerService;
import com.chaboshi.www.service.IProductsService;
import com.chaboshi.www.service.IProvinceCityService;
import com.chaboshi.www.service.IUserDetailService;
import com.chaboshi.www.util.URLParamHelper;
import com.chaboshi.www.vo.ProvinceCityVO;


// TODO: Auto-generated Javadoc
/**
 * ************************************
 * <a>页面展示---关于无关联页面展示</a>.
 *
 * @author ChaBoShi_Zhangjun
 * ************************************
 * 		1.0  页面展示
 * 
 * 		1.1 index 			展示首页
 * 		1.2 showSegement  	展示服务协议
 * 		1.3 showAboutus 	展示关于我们
 * 		1.4 showWhatVIN		展示什么是VIN
 * 		1.5 showResolveRule	展示解析规则页
 * 		1.6 showInviteGift  邀请好友注册页面
 * 		1.7	showInvitation  邀请好友页面
 * 		1.8	showMyMessage  	展示我的消息
 * 		1.9 AccountSettings 账户设置
 * 
 * ************************************
 * 修改历史：
 * 1.1	处理文本规范等相关事宜
 */
@Path("/wap")
public class WapHomeController extends BaseController {

	/** The Constant log. */
	public static final Logger log = LoggerFactory.getLogger(WapHomeController.class);
	


	/**
	 * <a>展示首页</a>.
	 *
	 * @return 返回WAP网站首页
	 * @throws Exception the exception
	 */
	@Path("/index")
	public ActionResult showIndex() throws Exception {
		log.info("展示首页");
		Object userPhone = beat().getRequest().getAttribute("USER_PHONE");
		IBannerService bannerService = ServiceInit.getService(IBannerService.class);
		IProductsService productsService = ServiceInit.getService(IProductsService.class);
		
		//用户城市ID选择
		if(userPhone!= null){
			IProvinceCityService provinceCityService = ServiceInit.getService(IProvinceCityService.class);
			IUserDetailService userDetailService = ServiceInit.getService(IUserDetailService.class);
			Long userId = getUserId(userPhone.toString());
			UserDetail userDetail = userDetailService.queryByUserId(userId);
			Integer cityId = userDetail.getCityId();
			if(cityId==null){
				Map<String, List<ProvinceCityVO>> wapFindCities = provinceCityService.wapFindCities();
				beat().getModel().add("selectCity", true);
				beat().getModel().add("provinces", wapFindCities);
			}
		}
		
		
		
		
		
		JSONObject productsInfo = new JSONObject();
		productsInfo.put("products", productsService.getProductsInfo(beat()));
		if(productsInfo.toString().contains("事故保")){
			beat().getModel().add("sgb", true);
		}
		if(productsInfo.toString().contains("车况保")){
			beat().getModel().add("ckb", true);
		}
		if(productsInfo.toString().contains("车价保")){
			beat().getModel().add("cjb", true);
		}
		log.info("获取轮播图片");
		List<Banner> banners = bannerService.getBanners(OrderSource.WAP);
		if(banners != null && banners.size() > 0) {
			log.info("获取到了轮播图片   bannners = " +banners);
			beat().getModel().add("banners", banners);
		}
		
		
		
		beat().getModel().add("user_name", userPhone);
		Enumeration<String> attributeNames = beat().getRequest().getSession().getAttributeNames();
		while(attributeNames.hasMoreElements()){
			beat().getRequest().getSession().removeAttribute(attributeNames.nextElement().toString());
		}
		return new MethodActionResult("/wap/index");
	}
	
	/**
	 * 显示查询页面.
	 *
	 * @return 返回WAP网站查询页面
	 */
	@Path("/search")
	public ActionResult showSearch() {
		log.info("展示查询页面");
		String mobile = getUserMobile();
		beat().getModel().add("user_name", mobile);
		return new MethodActionResult("/wap/search");
	}
	
	/**
	 * <a>展示服务协议</a>
	 * return 返回WAP网站的服务协议.
	 *
	 * @return the action result
	 */
	@Path("/showSegement")
	public ActionResult showSegement() {
		log.info("展示服务协议");
		beat().getModel().add("app", false);
		return new MethodActionResult("/wap/segement");
	}
	
	/**
	 * <a>展示关于我们</a>.
	 *
	 * @return 返回WAP网站的显示关于我们
	 */
	@Path("/showAboutus")
	public ActionResult showAboutus() {
		log.info("展示关于我们");
		return new MethodActionResult("/wap/aboutus");
	}

	/**
	 * <a>下载APP</a>.
	 *
	 * @return 显示下载APP页面
	 */
	@Path("/downloadAPP")
	public ActionResult downloadAPP() {
		log.info("显示下载APP页面");
		return new MethodActionResult("/wap/downloadAPP");
	}
	
	/**
	 * <a>展示什么是VIN</a>.
	 *
	 * @return 返回WAP网站VIN解释说明
	 */
	@Path("/showWhatVIN")
	public ActionResult showWhatVIN() {
		log.info("展示什么是VIN");
		return new MethodActionResult("/wap/whatVin");
	}
	
	/**
	 * <a>展示解析规则页</a>.
	 *
	 * @return 返回WAP网站解析规则页
	 */
	@Path("/showResolveRule")
	public ActionResult showResolveRule() {
		log.info("展示解析规则页");
		String source = URLParamHelper.getString(beat(),"source");
		String app = URLParamHelper.getString(beat(), "app");
		beat().getModel().add("isApp", app != null  || source != null);
		return new MethodActionResult("/wap/vehicle_report");
	}
	
	/**
	 * <a>展示错误页面</a>.
	 *
	 * @return 返回错误页面
	 */
	@Path("/showError")
	public ActionResult showError() {
		log.info("展示错误页面");
		return new MethodActionResult("/wap/error");
	}
	
	
	
	/**
	 * <a>展示解析规则</a>.
	 *
	 * @return 返回解析页面
	 */
	@Path("/showAppRule")
	public ActionResult showAppRule() {
		log.info("展示解析页面");
		return new MethodActionResult("/wap/vehicle_report_Copy");
	}
	
	
	/**
	 * <a>展示我的消息</a>.
	 *
	 * @return the action result
	 */
	@Path("/showMyMessage")
	public ActionResult showMyMessage() {
		return new MethodActionResult("/wap/message");
	}
	
	/**
	 * <a>展示账户设置</a>.
	 *
	 * @return the action result
	 */
	@Path("/AccountSettings")
	public ActionResult AccountSettings(){
		return new MethodActionResult("/wap/AccountSettings");
	}
	
	/**
	 * 免责条款.
	 *
	 * @return the action result
	 */
	@Path("/showFreelist")
	@SourceValidate
	public ActionResult showFreelist() {
		Object object = beat().getRequest().getAttribute("isapp");
		//判断是否移动端
		if(object!=null){
			beat().getModel().add("source", object.toString());
		}
		return new MethodActionResult("/wap/freelist");
	}
	

	/**
	 * 刮刮乐.
	 *
	 * @return the action result
	 */
	@Path("/cbsGGl")
	public ActionResult cbsGGl() {
		return new MethodActionResult("/wap/cbsGGl");
	}
	
	
	/**
	 * 车辆估价.
	 *
	 * @return the action result
	 */
	@Path("/valuationPrecise")
	public ActionResult valuationPrecise() {
		return new MethodActionResult("/wap/valuationPrecise");
	}
	
	
	/**
	 * 新闻资讯.
	 *
	 * @return the action result
	 */
	@Path("/news")
	public ActionResult news() {
		return new MethodActionResult("/wap/news");
	}
	
}
